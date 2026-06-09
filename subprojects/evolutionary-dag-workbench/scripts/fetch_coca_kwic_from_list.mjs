#!/usr/bin/env node

import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import process from "node:process";
import pkg from "/Users/brettreynolds/Documents/LLM-CLI-projects/tools/english-corpora/node_modules/playwright/index.js";

const { chromium } = pkg;

const ROOT = "https://www.english-corpora.org";
const TOOL_DIR = "/Users/brettreynolds/Documents/LLM-CLI-projects/tools/english-corpora";
const DEFAULT_PROFILE_DIR = path.join(os.homedir(), ".cache", "english-corpora-playwright");

function usage(exitCode = 0) {
  console.log(`Usage:
  node scripts/fetch_coca_kwic_from_list.mjs --query 'a bunch of people is' --output data/.../file.json

Options:
  --corpus coca          Corpus slug, default coca
  --query TEXT          Query text
  --output PATH         Output JSON path
  --hits N              List result rows, default 100
  --allow-partial       Save a bounded KWIC sample when the frame exposes fewer than ENTRIES
  --min-rows N          Minimum rows required with --allow-partial, default 1
  --headed              Show browser
`);
  process.exit(exitCode);
}

function parseArgs(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--help") usage(0);
    if (arg === "--headed" || arg === "--allow-partial") {
      out[arg.slice(2)] = true;
      continue;
    }
    if (!arg.startsWith("--")) throw new Error(`Unexpected argument: ${arg}`);
    const key = arg.slice(2);
    const value = argv[i + 1];
    if (value == null || value.startsWith("--")) throw new Error(`Missing value for --${key}`);
    out[key] = value;
    i += 1;
  }
  return out;
}

async function loadEnvFile(filePath) {
  let data;
  try {
    data = await fs.readFile(filePath, "utf8");
  } catch (error) {
    if (error.code === "ENOENT") return;
    throw error;
  }
  for (const rawLine of data.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) continue;
    const match = line.match(/^([A-Za-z_][A-Za-z0-9_]*)=(.*)$/);
    if (!match) continue;
    const [, key, rawValue] = match;
    if (process.env[key] != null) continue;
    let value = rawValue.trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    process.env[key] = value;
  }
}

async function loadEnvFiles() {
  await loadEnvFile(path.join(os.homedir(), ".config", "english-corpora", "env"));
  await loadEnvFile(path.join(TOOL_DIR, ".env"));
}

function normalizeCorpus(corpus = "coca") {
  const slug = String(corpus).trim().toLowerCase();
  if (!/^[a-z0-9_-]+$/.test(slug)) throw new Error(`Invalid corpus slug: ${corpus}`);
  return slug;
}

function profileDir() {
  return process.env.ENGLISH_CORPORA_PROFILE || DEFAULT_PROFILE_DIR;
}

async function bodyText(pageOrFrame) {
  try {
    return await pageOrFrame.locator("body").innerText({ timeout: 5000 });
  } catch {
    return "";
  }
}

async function waitForFrame(page, name, urlPart, timeoutMs = 30000) {
  const started = Date.now();
  while (Date.now() - started < timeoutMs) {
    const frame = page.frames().find((f) => f.name() === name && (!urlPart || f.url().includes(urlPart)));
    if (frame) return frame;
    await page.waitForTimeout(250);
  }
  throw new Error(`Timed out waiting for frame ${name}`);
}

async function waitForResultFrame(page, name, timeoutMs = 60000) {
  const started = Date.now();
  while (Date.now() - started < timeoutMs) {
    const frame = page.frames().find((f) => f.name() === name);
    if (frame && !/start2\.asp|about:blank$/i.test(frame.url())) {
      const ready = await frame.evaluate(() => document.readyState).catch(() => "");
      const text = await bodyText(frame);
      if (
        ready
        && /(\b\d+(?:\.\d+)?\s+seconds\b|ENTRIES:\s*\d+|Sorry, there are no matching records|Your session has expired|No more than one search every three seconds|There was an error on this page|You need to be registered to use the corpus)/i.test(text)
      ) return frame;
    }
    await page.waitForTimeout(500);
  }
  throw new Error(`Timed out waiting for result frame ${name}`);
}

async function isLoggedInWithPage(page, corpus) {
  await page.goto(`${ROOT}/${corpus}/x2.asp`, { waitUntil: "domcontentloaded", timeout: 30000 });
  const text = await bodyText(page);
  return !/You need to be registered to use the corpus/i.test(text);
}

async function loginWithCredentials(page) {
  const email = process.env.ENGLISH_CORPORA_EMAIL;
  const password = process.env.ENGLISH_CORPORA_PASSWORD;
  if (!email || !password) return false;
  await page.goto(`${ROOT}/login.asp`, { waitUntil: "domcontentloaded", timeout: 30000 });
  await page.locator('input[name="email"]').fill(email);
  await page.locator('input[name="password"]').fill(password);
  await Promise.all([
    page.waitForLoadState("domcontentloaded").catch(() => {}),
    page.locator('input[type="submit"]').first().click()
  ]);
  return true;
}

async function ensureLoggedIn(page, corpus) {
  if (await isLoggedInWithPage(page, corpus)) return;
  await loginWithCredentials(page);
  if (await isLoggedInWithPage(page, corpus)) return;
  throw new Error("English-Corpora.org session is not authenticated.");
}

function clean(text) {
  return String(text || "")
    .replace(/\u00a0/g, " ")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

async function extractFrame(frame) {
  return frame.evaluate(() => {
    const cleanLocal = (text) => String(text || "")
      .replace(/\u00a0/g, " ")
      .replace(/[ \t]+\n/g, "\n")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
    const tables = Array.from(document.querySelectorAll("table"))
      .map((table) => Array.from(table.rows)
        .map((row) => Array.from(row.cells).map((cell) => cleanLocal(cell.innerText)))
        .filter((row) => row.some(Boolean)))
      .filter((table) => table.length);
    const anchors = Array.from(document.querySelectorAll("a")).map((anchor) => ({
      text: cleanLocal(anchor.innerText),
      href: anchor.href,
      target: anchor.target || "",
      onclick: anchor.getAttribute("onclick") || "",
      id: anchor.id || ""
    }));
    return {
      url: location.href,
      title: document.title || "",
      text: cleanLocal(document.body?.innerText || ""),
      tables,
      anchors
    };
  });
}

function rowsFromKwicTables(tables) {
  const rows = [];
  for (const table of tables) {
    for (const cells of table) {
      if (cells.length < 5) continue;
      if (!/^\d+$/.test(cells[0])) continue;
      const hasTextId = /^\d+$/.test(cells[1]) && /^\d{4}$/.test(cells[2]);
      const yearIndex = hasTextId ? 2 : 1;
      if (!/^\d{4}$/.test(cells[yearIndex])) continue;
      const genreIndex = yearIndex + 1;
      const sourceIndex = yearIndex + 2;
      rows.push({
        index: Number(cells[0]),
        text_id: hasTextId ? cells[1] : "",
        year: cells[yearIndex],
        genre: cells[genreIndex],
        source: cells[sourceIndex],
        text: cells.slice(sourceIndex + 1).filter(Boolean).at(-1)?.replace(/\s+/g, " ").trim() || "",
        cells
      });
    }
  }
  return rows;
}

function expectedEntries(text) {
  const match = String(text || "").match(/ENTRIES:\s*(\d+)/i);
  return match ? Number.parseInt(match[1], 10) : null;
}

async function waitForKwicData(frame, timeoutMs = 45000, { allowPartial = false, minRows = 1 } = {}) {
  const started = Date.now();
  let last = null;
  while (Date.now() - started < timeoutMs) {
    const data = await extractFrame(frame);
    const rows = rowsFromKwicTables(data.tables);
    const expected = expectedEntries(data.text);
    last = { ...data, rows, expected };
    if (expected == null) {
      if (rows.length > 0 || /Sorry, there are no matching records/i.test(data.text)) return last;
    } else if (rows.length >= expected || /Sorry, there are no matching records/i.test(data.text)) {
      return last;
    }
    await frame.page().waitForTimeout(1000);
  }
  if (!last) throw new Error("Timed out waiting for KWIC data.");
  if (allowPartial && last.rows.length >= minRows) {
    return { ...last, partial: true };
  }
  const expected = last.expected == null ? "unknown" : String(last.expected);
  throw new Error(`Timed out waiting for complete KWIC rows: got ${last.rows.length}, expected ${expected}.`);
}

function assertUsable(text) {
  if (/You need to be registered to use the corpus/i.test(text)) {
    throw new Error("English-Corpora.org session is not authenticated.");
  }
  if (/Your session has expired/i.test(text)) {
    throw new Error("English-Corpora.org session expired during query.");
  }
  if (/No more than one search every three seconds/i.test(text)) {
    throw new Error("English-Corpora.org rate limit hit.");
  }
  if (/There was an error on this page/i.test(text)) {
    throw new Error("English-Corpora.org returned a server error page.");
  }
}

async function fetchKwic({ corpus, query, output, hits, headed, allowPartial, minRows }) {
  await loadEnvFiles();
  const context = await chromium.launchPersistentContext(profileDir(), {
    headless: !headed,
    viewport: { width: 1200, height: 900 },
    locale: "en-US"
  });

  try {
    const page = context.pages()[0] || await context.newPage();
    await ensureLoggedIn(page, corpus);
    await page.goto(`${ROOT}/${corpus}/`, { waitUntil: "domcontentloaded", timeout: 30000 });

    const x1 = await waitForFrame(page, "x1", "x1.asp");
    await x1.waitForSelector("form#zabba input#p", { timeout: 30000 });
    await x1.evaluate(({ query: queryText, hits: hitCount }) => {
      const byId = (id) => document.getElementById(id);
      const form = byId("zabba");
      const field = (id) => byId(id) || form?.elements?.namedItem(id);
      const setValue = (id, value) => {
        const el = field(id);
        if (!el) throw new Error(`Missing English-Corpora form field: ${id}`);
        el.value = value;
      };
      setValue("p", queryText);
      const numhits = field("numhits");
      if (numhits) numhits.value = String(hitCount);
      const target2 = window.top.frames.x2;
      if (target2) target2.location.href = "about:blank";
      const target3 = window.top.frames.x3;
      if (target3) target3.location.href = "about:blank";
    }, { query, hits });

    await x1.locator('input#submit1, input[type="submit"]').first().click();
    const x2 = await waitForResultFrame(page, "x2");
    const list = await extractFrame(x2);
    assertUsable(list.text);

    const resultLink = x2.locator('a[target="x3"]').filter({ hasText: new RegExp(`^${query.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}$`, "i") }).first();
    if (await resultLink.count() === 0) {
      throw new Error(`Could not find clickable list result for query: ${query}`);
    }
    await resultLink.click({ timeout: 10000 });

    const x3 = await waitForResultFrame(page, "x3");
    const kwic = await waitForKwicData(x3, 45000, { allowPartial, minRows });
    assertUsable(kwic.text);

    const result = {
      query,
      corpus,
      retrieved_at: new Date().toISOString(),
      method: "list-result-click",
      list: {
        url: list.url,
        text: list.text,
        tables: list.tables
      },
      kwic: {
        url: kwic.url,
        text: kwic.text,
        tables: kwic.tables,
        rows: kwic.rows,
        partial: Boolean(kwic.partial),
        expected: kwic.expected
      }
    };

    await fs.mkdir(path.dirname(path.resolve(output)), { recursive: true });
    await fs.writeFile(output, `${JSON.stringify(result, null, 2)}\n`);
  } finally {
    await context.close();
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const corpus = normalizeCorpus(args.corpus || "coca");
  const query = clean(args.query);
  if (!query) throw new Error("--query is required");
  if (!args.output) throw new Error("--output is required");
  const hits = Number.parseInt(args.hits || "100", 10);
  if (!Number.isFinite(hits) || hits < 1) throw new Error(`Invalid --hits: ${args.hits}`);
  const minRows = Number.parseInt(args["min-rows"] || "1", 10);
  if (!Number.isFinite(minRows) || minRows < 1) throw new Error(`Invalid --min-rows: ${args["min-rows"]}`);
  await fetchKwic({
    corpus,
    query,
    output: args.output,
    hits,
    headed: Boolean(args.headed),
    allowPartial: Boolean(args["allow-partial"]),
    minRows
  });
}

main().catch((error) => {
  console.error(`fetch_coca_kwic_from_list: ${error.message}`);
  process.exit(1);
});
