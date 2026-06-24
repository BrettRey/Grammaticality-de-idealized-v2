#!/bin/bash
# Sequential Gemini extraction with delays to avoid rate limits
cd /Users/brettreynolds/Documents/LLM-CLI-projects/papers/Grammaticality_de_idealized/subprojects/etiological-account/literature

echo "Starting sequential extraction at $(date)"

# 1. Lewis - Coordination and Convention
echo "[1/12] Lewis: Coordination and Convention"
gemini --yolo "Read the file 'Convention - 2002 - Lewis - Coordination and Convention.pdf' in this directory. Extract passages on: 1. COORDINATION PROBLEMS - definition, examples 2. COORDINATION EQUILIBRIA - what they are, how they arise 3. SALIENCE - how some equilibria become focal. For each passage: quote exact text, note page number, explain relevance to linguistic conventions. Output as markdown." > lewis-coordination.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 2. Lewis - Convention Refined
echo "[2/12] Lewis: Convention Refined"
gemini --yolo "Read the file 'Convention - 2002 - Lewis - Convention Refined.pdf' in this directory. Extract passages on: 1. DEFINITION OF CONVENTION - Lewis's formal definition 2. COMMON KNOWLEDGE - role in convention 3. REGULARITY - how conventions are regularities in behavior. For each passage: quote exact text, note page number. Output as markdown." > lewis-refined.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 3. Lewis - Conventions of Language
echo "[3/12] Lewis: Conventions of Language"
gemini --yolo "Read the file 'Convention - 2002 - Lewis - Conventions of Language.pdf' in this directory. Extract passages on: 1. LINGUISTIC CONVENTIONS - how language is conventional 2. MEANING AS CONVENTION - conventional form-meaning pairings 3. LANGUAGE COMMUNITIES - shared conventions. For each passage: quote exact text, note page number. Output as markdown." > lewis-language.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 4. O'Connor ch2
echo "[4/12] O'Connor: Chapter 2"
gemini --yolo "Read the file 'oso-9780198789970-chapter-2.pdf' in this directory. This is from O'Connor's 'Origins of Unfairness'. Extract passages on: 1. COORDINATION GAMES - basic setup 2. CONVENTIONS - how they emerge from coordination 3. EQUILIBRIUM SELECTION - why one convention wins. For each passage: quote exact text, note page number. Output as markdown." > oconnor-ch2.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 5. O'Connor ch3
echo "[5/12] O'Connor: Chapter 3"
gemini --yolo "Read the file 'oso-9780198789970-chapter-3.pdf' in this directory. This is from O'Connor's 'Origins of Unfairness'. Extract passages on: 1. SELF-REINFORCING CONVENTIONS - why they persist 2. NORM ENFORCEMENT - penalties for deviation 3. EXCLUSION - how coordination can exclude options. For each passage: quote exact text, note page number. Output as markdown." > oconnor-ch3.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 6. O'Connor ch4
echo "[6/12] O'Connor: Chapter 4"
gemini --yolo "Read the file 'oso-9780198789970-chapter-4.pdf' in this directory. This is from O'Connor's 'Origins of Unfairness'. Extract passages on: 1. CONVENTION PERSISTENCE - why established conventions persist 2. DEVIATION PENALTIES - costs of not conforming 3. EQUILIBRIUM STABILITY - what keeps equilibria stable. For each passage: quote exact text, note page number. Output as markdown." > oconnor-ch4.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 7. Young 1993
echo "[7/12] Young 1993"
gemini --yolo "Read the file 'Young-EvolutionConventions-1993.pdf' in this directory. This is Young's Econometrica paper on convention evolution. Extract passages on: 1. MATHEMATICAL MODEL - how conventions evolve 2. CONVERGENCE - why populations converge to conventions 3. STABILITY - what makes conventions stable. For each passage: quote exact text, note page number. Output as markdown." > young-1993.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 8. Skyrms ch1
echo "[8/12] Skyrms: Signals ch1"
gemini --yolo "Read the file '143883583.pdf' in this directory. This is from Skyrms's 'Signals'. Extract passages on: 1. SIGNALING GAMES - basic setup 2. SENDER-RECEIVER - how signals coordinate action 3. CONVENTION EMERGENCE - how signaling conventions arise. For each passage: quote exact text, note page number. Output as markdown." > skyrms-ch1.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 9. Powell ch1
echo "[9/12] Powell: Chapter (cab)"
gemini --yolo "Read the file '9780262356596_cab.pdf' in this directory. This is from Powell's 'Contingency and Convergence'. Extract passages on: 1. CONTINGENCY vs CONVERGENCE - definitions 2. CONVERGENT SOLUTIONS - what makes outcomes convergent 3. CONSTRAINTS - what channels outcomes toward convergence. For each passage: quote exact text, note page number. Output as markdown." > powell-ch1.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 10. Powell ch2
echo "[10/12] Powell: Chapter (caf)"
gemini --yolo "Read the file '9780262356596_caf.pdf' in this directory. This is from Powell's 'Contingency and Convergence'. Extract passages on: 1. BOTTOM-UP processes - emergence from local interactions 2. NORM ENFORCEMENT - distributed enforcement 3. SOCIAL INSECTS - if mentioned, extract fully. For each passage: quote exact text, note page number. Output as markdown." > powell-ch2.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 11. Boyd & Richerson 1985
echo "[11/12] Boyd & Richerson 1985"
gemini --yolo "Read the file 'Culture and the Evolutionary Process -- Peter J_ Richerson, Robert Boyd -- First Edition, 1988 -- Chicago_ University of Chicago Press -- 9780226069319 -- d160556f92f968434a48561aa5af076c -- Anna'\''s Archive.pdf' in this directory. This is a full book. Focus on extracting passages about: 1. FREQUENCY-DEPENDENT BIAS - when common variants are favored 2. CONFORMIST TRANSMISSION - copying the majority 3. CULTURAL STABILITY - what makes cultural traits persist. For each passage: quote exact text, note page number. Output as markdown." > boydricherson-1985.md 2>&1
echo "Done. Sleeping 45s..."
sleep 45

# 12. Richerson & Boyd 2005
echo "[12/12] Richerson & Boyd 2005"
gemini --yolo "Read the file 'Not By Genes Alone _ How Culture Transformed Human Evolution -- Peter J_ Richerson, Boyd, Robert, Robert Boyd - -- December 31, 2004 -- University Of -- 9780226712123 -- 99d4e08895446dfea3e1fb2f012da7a9 -- Anna'\''s .pdf' in this directory. This is a full book. Focus on extracting passages about: 1. NORM ENFORCEMENT - how norms are enforced 2. PUNISHMENT OF DEVIANTS - costs of non-conformity 3. CONFORMIST BIAS - preference for common behaviors. For each passage: quote exact text, note page number. Output as markdown." > boydricherson-2005.md 2>&1

echo "All extractions complete at $(date)"
