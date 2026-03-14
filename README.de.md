<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">中文</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.ja.md">日本語</a> |
  <strong>Deutsch</strong>
</p>

# Ramadan AI AI-Agententeam

**Automatisierte End-to-End-IT-Projektabwicklung durch spezialisierte, orchestrierte KI-Agenten.**

Ramadan AI transformiert den Software-Delivery-Lifecycle in ein System komponierbarer AI Agent Skills. Jede Aufgabe im Projektlebenszyklus — von der Projektcharta bis zur Post-Release-Retrospektive — wird als strukturierter Skill mit eigenem SOP, Definition of Ready (DoR), Definition of Done (DoD), RACI-Matrix und Werkzeugreferenzen kodifiziert. Ein Multi-Agenten-Team führt diese Skills unter Orchestrierung aus und erzeugt prüfbare, qualitätsgesicherte Arbeitsergebnisse in jeder Phase.

---

## Inhaltsverzeichnis

- [Motivation](#motivation)
- [Kernkonzepte](#kernkonzepte)
- [Agententeam](#agententeam)
- [Skill-Anatomie](#skill-anatomie)
- [Delivery-Playbook](#delivery-playbook)
- [Ausführungsmodell](#ausführungsmodell)
- [Projektstruktur](#projektstruktur)
- [Erste Schritte](#erste-schritte)
- [Vertiefung: Project Structure Scan und Agentengedächtnis](#vertiefung-project-structure-scan-und-agentengedächtnis)
- [Mitwirken](#mitwirken)
- [Lizenz](#lizenz)

---

## Motivation

IT-Projekte im Unternehmensumfeld folgen etablierten Lebenszyklusphasen — Inception, Requirements, Development, QA und Release — dennoch verteilt sich das operative Wissen für jede einzelne Aufgabe typischerweise auf verstreute Wikis, implizites Erfahrungswissen oder Ad-hoc-Checklisten. Ramadan AI adressiert dieses Problem durch:

1. **Zerlegung des Delivery-Lebenszyklus** in diskrete, klar definierte Aufgaben über alle Phasen hinweg.
2. **Kodifizierung jeder Aufgabe als AI Agent Skill** mit formalen Qualitätsdimensionen (SOP, DoR, DoD, RACI, Tools).
3. **Orchestrierung der Skill-Ausführung** durch eine ereignisgesteuerte Multi-Agenten-Architektur mit integrierten Supervisor-Qualitätstoren.

Das Ergebnis ist ein reproduzierbares, nachvollziehbares und kontinuierlich verbesserungsfähiges Delivery-System, das von KI-Agenten betrieben wird.

---

## Kernkonzepte

### Skill-per-Task-Modell

Jede Aufgabe im Software-Delivery-Lifecycle wird genau einem AI Agent Skill zugeordnet. Ein Skill ist kein generischer Prompt — er ist eine strukturierte Ausführungseinheit, die Folgendes enthält:

| Dimension | Zweck | Beispiel |
|:---|:---|:---|
| **SOP** | Schrittweise Verfahrensanweisung (Phase 0–5) | Durchführung einer technischen Discovery-Bewertung |
| **DoR** | Voraussetzungen, die vor Ausführungsbeginn erfüllt sein müssen | Scope definiert, Stakeholder identifiziert, Werkzeuge verfügbar |
| **DoD** | Qualitätscheckliste, die bestanden sein muss, bevor die Aufgabe als abgeschlossen gilt | 19-Punkte-Checkliste für Arbeitsergebnisse, Prozess und Dokumentation |
| **RACI** | Verantwortlichkeitszuordnung für alle Beteiligten | SA = Responsible, PM = Accountable, TL = Consulted |
| **Tools** | Werkzeugreferenzen und Nutzungshinweise | WebSearch, Dateioperationen, Diagrammgeneratoren |
| **Triggers** | Bedingungen, die den Skill aktivieren | Abschluss vorgelagerter Aufgaben, PM-Anweisung |
| **Output Templates** | Standardisierte Ergebnisformate | Berichtsstruktur, Entscheidungsprotokollformat |

### Supervisor-Qualitätstore

Jeder Haupt-Skill verfügt über einen gepaarten **Supervisor-Skill**, der eine unabhängige Qualitätsprüfung durchführt. Eine Aufgabe gilt erst dann als abgeschlossen, wenn der Supervisor eine Bestehensquote von 100 % über alle Prüfkriterien erreicht hat. Fehlgeschlagene Punkte lösen eine automatische Nachbesserung und erneute Prüfung aus.

### Ereignisgesteuerte Orchestrierung

Agenten kommunizieren über ein strukturiertes Ereignisprotokoll:

```
PM broadcasts TaskTriggered → Role Agent executes skill → Self-check DoD
  → Supervisor inspects → 100% pass → TaskCompleted reported to PM
  → PM triggers downstream tasks
```

---

## Agententeam

Ramadan AI arbeitet als Vier-Agenten-Team, wobei jeder Agent eine klar abgegrenzte Rolle und ein eigenes Skill-Portfolio besitzt:

| Agent | Rolle | Typ | Skills | Abdeckung |
|:---|:---|:---|:---:|:---|
| **PM Agent** | Projektmanager | Orchestrator | 24 | Charta, Stakeholder-Analyse, Ressourcenplanung, Risikomanagement, Release-Koordination, Projektabschluss |
| **IPM Agent** | IT-Produktmanager | Role Agent | 21 | Anforderungserhebung, BRD-/PRD-Erstellung, User Stories, Abnahmekriterien, UAT, Launch-Koordination |
| **SA Agent** | Systemarchitekt | Role Agent | 37 | Technische Discovery, Architekturdesign, NFRs, Integrationsdesign, Sicherheitsreview, Deployment-Architektur |
| **TL Agent** | Technical Lead | Role Agent | 24 | Technische Vision, Lösungsdesign, Code-Review-Leitung, Entwicklungsstandards, Technische Risikobewertung |

Jeder Haupt-Skill besitzt einen gepaarten Supervisor, wodurch sich insgesamt **212 Skill-Verzeichnisse** (106 Haupt-Skills + 106 Supervisors) ergeben.

---

## Skill-Anatomie

Jeder Skill folgt einer standardisierten Verzeichnisstruktur:

```
{role}-{skill-name}/
├── SKILL.md                        # Skill-Definition mit Phase-0–5-Workflow
└── references/
    ├── sop.md                      # Standard Operating Procedure
    ├── dor.md                      # Definition of Ready
    ├── dod.md                      # Definition of Done
    ├── raci.md                     # RACI-Matrix
    ├── tools.md                    # Werkzeugreferenz
    ├── triggers.md                 # Aktivierungsbedingungen
    ├── output-templates.md         # Ergebnisvorlagen
    └── skills-and-knowledge.md     # Erforderliche Kompetenzen
```

Supervisor-Skills ergänzen eine Datei `inspection-criteria.md` sowie ein automatisiertes Verifizierungsskript `scripts/verify_dod.py`.

### Universeller Phase-0–5-Workflow

Jeder Skill durchläuft denselben sechsphasigen Workflow, um Konsistenz sicherzustellen:

| Phase | Bezeichnung | Zweck |
|:---:|:---|:---|
| 0 | Initialisierung | Ausgabeverzeichnis erstellen, Protokolle initialisieren, DoR verifizieren |
| 1 | Aufgabenzweck verstehen | Ziele durch Dialog klären, Benutzerbestätigung einholen |
| 2 | Themenverständnis vertiefen | Fachlichen Kontext vertiefen, Hintergrundinformationen sammeln |
| 3 | Recherche und Rückfragen | Branchenrecherche, iterative Fragengenerierung, Expertenkonsultation |
| 4 | Ausführung und Lieferung | Arbeitsergebnisse mit Vorlagen erstellen, Selbstprüfung gegen DoD |
| 5 | Abschluss und Übergabe | Supervisor aufrufen, Mängel beheben, Bericht an PM |

---

## Delivery-Playbook

Das [`delivery_playbook.md`](task/delivery_playbook.md) definiert die vollständige Aufgabenreihenfolge über fünf Projektphasen, organisiert in sequenzielle Wellen:

### Phasen und Aufgabenverteilung

| Phase | Beschreibung | Kerntätigkeiten |
|:---|:---|:---|
| **Inception** | Projektinitiierung und Machbarkeitsprüfung | Charta-Entwicklung, Stakeholder-Analyse, Anforderungserhebung, Technologieauswahl, Risikoidentifikation |
| **Requirements** | Detailspezifikation und Design | Architekturdesign, NFR-Definition, Integrationsdesign, Datenarchitektur, PRD-Erstellung, Technische Standards |
| **Development** | Implementierung und technische Steuerung | Code-/Design-Reviews, Spike-/PoC-Leitung, Technical-Debt-Management, ADR-Dokumentation |
| **QA** | Validierung und Compliance | Performancetests, Sicherheitsreview, Compliance-Validierung, Infrastrukturvalidierung, UAT-Koordination |
| **Release** | Deployment und Stabilisierung | Deployment-Architektur, Monitoring-Einrichtung, Kapazitätsplanung, Go-Live-Koordination, Hypercare, Retrospektiven |

### Wellenbasiertes Ausführungsmodell

Aufgaben innerhalb einer Welle werden parallel ausgeführt. Alle Aufgaben in Welle N müssen abgeschlossen sein, bevor Welle N+1 beginnt. Dies ermöglicht maximale Parallelisierung bei gleichzeitiger Einhaltung von Aufgabenabhängigkeiten.

---

## Ausführungsmodell

### Ereignisprotokoll

| Ereignis | Richtung | Nutzlast |
|:---|:---|:---|
| `TaskTriggered` | PM → Role Agent | `{ task_id, skill_dir, inputs, context }` |
| `TaskCompleted` | Role Agent → PM | `{ task_id, status, artifacts, supervisor_report }` |
| `SupervisorTriggered` | Role Agent → Supervisor | `{ task_id, output_dir }` |
| `SupervisorCompleted` | Supervisor → Role Agent | `{ task_id, pass_rate, report, remediation_items }` |

### Qualitätssicherungsablauf

```
Role Agent schließt Skill-Ausführung ab
       │
       ▼
Selbstprüfung: Alle 19 DoD-Punkte verifizieren
       │
       ├── FAIL → Automatische Nachbesserung, erneute Verifizierung
       │
       ▼
Gepaarten Supervisor-Skill aufrufen
       │
       ├── FAIL → Nachbesserungsbericht empfangen, beheben, Supervisor erneut aufrufen
       │
       ▼
100 % Bestehensquote erreicht → TaskCompleted an PM melden
```

### Idempotenz

Jede Aufgabenausführung ist idempotent. Das System verfolgt den Aufgabenstatus (`PENDING`, `IN_PROGRESS`, `DONE`, `FAILED`) und setzt die Verarbeitung fort oder überspringt sie entsprechend, wodurch doppelte Arbeit vermieden und eine zuverlässige Wiederherstellung ermöglicht wird.

---

## Projektstruktur

```
ramadan/
├── IDENTITY.md                     # Teamidentitätsdefinition
├── SOUL.md                         # Team-Persona und operative Grenzen
├── AGENTS.md                       # Agentenregistrierung und Ereignisprotokoll
├── USER.md                         # Benutzerinteraktionsmodell
├── TOOLS.md                        # Werkzeugnutzungskonventionen
│
├── config/
│   ├── agents-registry.json        # Agentendefinitionen und Metadaten
│   ├── openclaw.json               # Skill-Bindungen, Tool-Profile, Event-Bus-Konfiguration
│   └── event-bus.json              # Ereignis-Routing-Regeln
│
├── pm-*/                           # 24 PM-Skills + 24 Supervisors
├── ipm-*/                          # 21 IPM-Skills + 21 Supervisors
├── sa-*/                           # 37 SA-Skills + 37 Supervisors
├── tl-*/                           # TL-Skills + Supervisors
│
├── task/
│   ├── delivery_playbook.md        # Vollständige Aufgabenausführungsreihenfolge
│   └── *_agent_skill_definition.md # Skill-Spezifikationen auf Aufgabenebene
│
├── prompt/
│   ├── generate_team.py            # Team-Scaffolding-Generator
│   └── openclaw-skill-creator-prompt.md  # Skill-Erstellungsleitfaden
│
├── openclaw-team/                  # Deploymentfähiges Teampaket
│   ├── skills/                     # Alle Skills konsolidiert
│   ├── workspaces/                 # Agenten-Workspace-Vorlagen
│   ├── scripts/
│   │   ├── install_team.py         # Ein-Klick-Installer
│   │   ├── quick_validate.py       # Strukturvalidierung
│   │   ├── init_skill.py           # Neuer Skill-Scaffolder
│   │   └── package_skill.py        # Skill-Paketierung
│   └── config/                     # Deployment-Konfiguration
│
└── scripts/
    ├── install_team.py             # Team-Deployment-Skript
    ├── bootstrap_workspaces.py     # Workspace-Initialisierung
    └── package_team.py             # Distributionspaketierung
```

---

## Erste Schritte

### Voraussetzungen

- Python 3.8+
- Claude Code CLI mit Zugang zum Claude Opus 4.6 Modell
- Git

### Installation

1. **Repository klonen**
   ```bash
   git clone <repository-url>
   cd ramadan
   ```

2. **Teampaket installieren**
   ```bash
   python scripts/install_team.py
   ```

3. **Agenten-Workspaces initialisieren**
   ```bash
   python scripts/bootstrap_workspaces.py
   ```

4. **Skill-Struktur validieren**
   ```bash
   python openclaw-team/scripts/quick_validate.py
   ```

### Einen neuen Skill erstellen

Verwenden Sie das Skill-Scaffolding-Werkzeug, um einen neuen Skill mit allen erforderlichen Referenzdateien zu generieren:

```bash
python openclaw-team/scripts/init_skill.py --role sa --name my-new-skill
```

Dieser Befehl erstellt die vollständige Verzeichnisstruktur mit Vorlagendateien für SOP, DoR, DoD, RACI, Tools, Triggers und Output Templates.

---

## Vertiefung: Project Structure Scan und Agentengedächtnis

Der **Project Structure Scan** Skill (`project-structure-scan`) ist der architektonisch fortschrittlichste Skill in Ramadan AI. Er dient als Referenzimplementierung für eine Schlüsselfähigkeit, die den meisten AI Agent Skills fehlt: **persistentes, strukturiertes Gedächtnis, das über Sitzungen hinweg erhalten bleibt und Wissen projektübergreifend transferiert**.

### Das Problem: Zustandslose KI-Agenten

Standardmäßig sind KI-Agenten zustandslos. Jede Konversation beginnt bei null. Wenn ein Agent heute eine Codebasis analysiert und der Benutzer nächste Woche zurückkehrt, um dasselbe Projekt erneut zu scannen, hat der Agent keinerlei Erinnerung an frühere Ergebnisse, kein Bewusstsein für Veränderungen und keine Möglichkeit, redundante Arbeit zu überspringen. Dies führt zu:

- Wiederholter Analyse von unverändertem Code
- Erneutem Stellen von Fragen, die der Benutzer bereits beantwortet hat
- Fehlender Nachverfolgung der Projektentwicklung über die Zeit
- Fehlendem projektübergreifenden Lernen (Erkenntnisse aus Projekt A kommen Projekt B nie zugute)

Der Project Structure Scan Skill löst dieses Problem mit einem **SQLite-basierten Gedächtnissystem**, das den Agenten mit jeder Ausführung progressiv intelligenter macht.

### Gedächtnisarchitektur

Das Gedächtnissystem verwendet eine lokale SQLite-Datenbank (`memory/agent_memory.db`) mit vier zweckgebundenen Tabellen:

```
┌─────────────────────────────────────────────────────────────┐
│                    agent_memory.db                           │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ task_memory  │  │ knowledge    │  │   scan_history    │  │
│  │             │  │ _base        │  │                   │  │
│  │ findings    │  │              │  │ session tracking  │  │
│  │ decisions   │  │ patterns     │  │ scope & status    │  │
│  │ lessons     │  │ dependencies │  │ deliverables path │  │
│  │ questions   │  │ tech_stack   │  │ timestamps        │  │
│  │ risks       │  │ conventions  │  │                   │  │
│  │             │  │ insights     │  │                   │  │
│  │ (per phase, │  │              │  │                   │  │
│  │  per session)│  │ (confidence  │  │                   │  │
│  │             │  │  scored,     │  │                   │  │
│  │             │  │  cross-      │  │                   │  │
│  │             │  │  project)    │  │                   │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
│                                                             │
│  ┌─────────────┐                                            │
│  │ dod_checks  │    Supplementary Files:                    │
│  │             │    ├── logs/conversation-log.md             │
│  │ per-round   │    ├── logs/work-log.md                    │
│  │ pass/fail   │    ├── research/{topic}.md                 │
│  │ evidence    │    └── phase{N}-questions.md                │
│  └─────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
```

| Tabelle | Zweck | Schlüsselfelder |
|:---|:---|:---|
| `task_memory` | Sitzungsbezogene Ergebnisse, Entscheidungen, Erkenntnisse, Fragen und Risiken | `session_id`, `phase`, `memory_type`, `content`, `tags` |
| `knowledge_base` | Sitzungsübergreifend wiederverwendbares Wissen mit Konfidenzwerten | `category`, `key`, `value`, `confidence` (0.0–1.0) |
| `scan_history` | Revisionssichere Protokollierung jeder Scan-Ausführung | `project_name`, `scan_scope`, `status`, `deliverables_path` |
| `dod_checks` | Ergebnisse der Qualitätssicherungsprüfung je Durchlauf | `check_round`, `check_item`, `status`, `evidence` |

### Integration des Gedächtnissystems in die einzelnen Workflow-Phasen

Das Gedächtnissystem ist kein nachträglich angebundenes Feature — es ist in jede Phase der Skill-Ausführung eingewoben:

**Phase 0 — Gedächtnisgesteuerte Initialisierung**

Beim Start fragt der Agent `scan_history` ab, um festzustellen, ob dieses Projekt bereits gescannt wurde. Diese einzelne Abfrage bestimmt den gesamten Ausführungspfad:

```
load_project_history(project_name)
  │
  ├── Previous scans found → Re-scan Mode
  │   └── generate_memory_summary() → present to user
  │       └── User chooses: Incremental / Full re-scan / Review previous
  │
  ├── No history, but similar projects exist → Hypothesis Mode
  │   └── get_similar_projects(tech_stack_tags)
  │       └── "Project X used DDD with Hexagonal. Look for similar patterns?"
  │
  └── No history, no similar projects → Fresh Scan Mode
```

Bevor die eigentliche Arbeit beginnt, führt der Agent außerdem Wartungsoperationen durch: `apply_confidence_decay()` reduziert den Konfidenzwert von Wissenseinträgen, die seit 90 Tagen nicht aktualisiert wurden, und `prune_low_confidence()` entfernt Einträge, deren Konfidenz unter den Schwellenwert von 0,3 gefallen ist.

**Phase 1 — Gedächtnisgestütztes Aufgabenverständnis**

Anstatt den Benutzer jedes Mal von Neuem zu fragen „Warum benötigen Sie diesen Scan?", fragt der Agent frühere Zweckeinträge ab:

```python
load_lessons_learned(task_id='SA-DISC-001', project_name=...) # filtered by phase='phase1'
```

Wenn Einträge vorhanden sind, präsentiert er: *„Beim letzten Scan dieses Projekts war der Zweck: {previous_purpose}. Ist der Zweck dieses Mal derselbe?"* — und reduziert damit einen fünfminütigen Dialog auf eine einzelne Bestätigung.

**Phase 2 — Gedächtnisbeschleunigte Discovery**

Der Agent fragt die `knowledge_base` nach zuvor erfasstem Technologie-Stack, Mustern und Konventionen ab:

```python
load_project_knowledge(project_name)  # returns entries sorted by confidence DESC
```

Bekannte Antworten werden vorausgefüllt. Nur Delta-Fragen — Aspekte, die unbekannt sind oder sich verändert haben könnten — werden gestellt. Bei erneuten Scans eliminiert dies 60–80 % der Fragen.

**Phase 3 — Gedächtnisinformierte Recherche**

Frühere Recherchedateien und Risikoeinträge werden geladen. Der Agent überspringt redundante Recherchen, konzentriert sich auf Lücken und überprüft proaktiv bekannte Risiken: *„Beim letzten Mal habe ich folgende Risiken identifiziert: {Liste}. Soll ich überprüfen, ob diese behoben wurden?"*

**Phase 4 — Gedächtnisoptimierte Ausführung**

Bei inkrementellen Scans lädt der Agent den vorherigen `OUT-01` (Project Structure Tree), vergleicht ihn mit der aktuellen Verzeichnisstruktur und analysiert nur geänderte Bereiche im Detail. Der vorherige `OUT-04` (Package Dependency Map) wird mit dem aktuellen Manifest abgeglichen, um einen rein änderungsbasierten Abhängigkeitsbericht zu erstellen. Dies reduziert die Ausführungszeit bei erneuten Scans um 40–70 %.

### Projektübergreifender Wissenstransfer

Die leistungsfähigste Gedächtnisfunktion operiert über Projektgrenzen hinweg. Wenn der Agent auf ein neues Projekt trifft, durchsucht er die Wissensdatenbank nach Projekten mit ähnlichem Technologie-Stack:

```python
get_similar_projects(db_path, tech_stack_tags=["spring-boot", "postgresql", "redis"])
# Returns: [{"project_name": "ProjectX", "matching_tags": [...], "match_count": 3}]
```

Hochkonfidente Muster aus ähnlichen Projekten werden zu Hypothesen für das neue Projekt. Wenn der Agent zuvor erkannt hat, dass drei Spring-Boot-Projekte alle ein Hexagonal-Architecture-Muster verwenden, kann er proaktiv fragen: *„Ähnliche Projekte in meinen Aufzeichnungen verwenden Hexagonal Architecture. Soll ich nach diesem Muster suchen?"* — und beschleunigt damit die Erstanalyse um etwa 30 %.

### Konfidenzverfall und Widerspruchserkennung

Wissen bleibt nicht unbegrenzt gültig. Das Gedächtnissystem implementiert zwei Mechanismen zur Wahrung der Integrität:

1. **Konfidenzverfall**: Alle 90 Tage verlieren Einträge, die nicht aktualisiert wurden, 0,2 Konfidenzpunkte (Minimum 0,0). Ein Eintrag mit einem Konfidenzwert von 0,8 fällt über aufeinanderfolgende Perioden auf 0,6 → 0,4 → 0,2 → 0,0, sofern er nie bestätigt wird. Einträge unter 0,3 werden bereinigt und dem Benutzer gemeldet.

2. **Widerspruchserkennung**: Vor dem Schreiben eines neuen Wissenseintrags prüft der Agent auf Konflikte:

   ```python
   contradiction = detect_contradictions(db_path, project_name, category, key, new_value)
   # Returns existing vs. new value if they differ
   ```

   Wenn ein Widerspruch erkannt wird (z. B. das Architekturmuster wurde zuvor als „MVC" erfasst, neue Evidenz deutet jedoch auf „Hexagonal" hin), markiert der Agent den Konflikt und bittet den Benutzer um Klärung — anstatt den Eintrag stillschweigend zu überschreiben.

### API für Gedächtnisoperationen

Alle Gedächtnisoperationen sind in `scripts/memory_ops.py` als reine Funktionen mit expliziten Datenbankpfadparametern implementiert:

| Operation | Funktion | Verwendungszeitpunkt |
|:---|:---|:---|
| Scan-Verlauf laden | `load_project_history()` | Phase 0 — Scan-Modus bestimmen |
| Wissen laden | `load_project_knowledge()` | Phase 1–4 — bekannte Antworten vorausfüllen |
| Erkenntnisse laden | `load_lessons_learned()` | Phase 1–3 — redundante Arbeit überspringen |
| Ähnliche Projekte finden | `get_similar_projects()` | Phase 0 — projektübergreifender Transfer |
| Zusammenfassung generieren | `generate_memory_summary()` | Phase 0 — Verlauf dem Benutzer präsentieren |
| Ergebnis erfassen | `record_finding()` | Phase 4 — Scan-Ergebnisse persistieren |
| Entscheidung erfassen | `record_decision()` | Phase 1–3 — bestätigte Entscheidungen persistieren |
| Risiko erfassen | `record_risk()` | Phase 3–4 — identifizierte Risiken persistieren |
| Wissen erfassen | `record_knowledge()` | Alle Phasen — UPSERT in die Wissensdatenbank |
| Erkenntnis erfassen | `record_lesson()` | Phase 5 — Sitzungserkenntnisse festhalten |
| Scan starten/abschließen | `start_scan()` / `complete_scan()` | Phase 0/5 — Scan-Lebenszyklus |
| DoD-Prüfung erfassen | `record_dod_check()` | Phase 4 — Qualitätssicherungsergebnisse |
| Verfall anwenden | `apply_confidence_decay()` | Phase 0 — Aktualität sicherstellen |
| Widersprüche erkennen | `detect_contradictions()` | Vor jedem Wissensschreibvorgang |
| Niedrige Konfidenz bereinigen | `prune_low_confidence()` | Phase 0 — veraltete Einträge entfernen |

### Skill-Verzeichnisstruktur

Der Project Structure Scan Skill erweitert die Standard-Skill-Anatomie um dedizierte Verzeichnisse für Gedächtnis, Recherche und Vorlagen:

```
project-structure-scan/
├── SKILL.md                          # Skill-Definition (gedächtniserweiterte Phase 0–5)
├── memory/
│   ├── index.md                      # Dokumentation der Gedächtnisarchitektur
│   └── agent_memory.db               # SQLite-Datenbank (wird zur Laufzeit erstellt)
├── config/
│   ├── triggers.md                   # Projektaufnahme-Checkliste (7 Punkte)
│   ├── raci.md                       # RACI-Matrix mit nachgelagerten Triggern
│   ├── tools.md                      # Werkzeugreferenz
│   ├── mcp-tools.md                  # MCP-Werkzeugkonfigurationen
│   └── skills-and-knowledge.md       # Erforderliche Agentenkompetenzen
├── references/
│   ├── sop.md                        # Standard Operating Procedure
│   ├── dor.md                        # Definition of Ready
│   ├── dod.md                        # Definition of Done
│   └── output-templates.md           # Vorlagenindex
├── templates/
│   ├── structure-tree-template.md    # OUT-01-Vorlage
│   ├── module-relationship-template.md # OUT-02-Vorlage
│   ├── layering-analysis-template.md # OUT-03-Vorlage
│   ├── dependency-map-template.md    # OUT-04-Vorlage
│   ├── module-summary-template.md    # OUT-05-Vorlage
│   └── scan-report-template.md       # OUT-06-Vorlage
├── scripts/
│   ├── init_memory.py                # Datenbankschema-Initialisierung
│   ├── memory_ops.py                 # Gedächtnis-CRUD-Operationsbibliothek
│   └── verify_dod.py                 # Automatisierte DoD-Verifizierung
├── research/                         # Rechercheartefakte (werden zur Laufzeit befüllt)
├── logs/                             # Ausführungsprotokolle (werden zur Laufzeit befüllt)
└── diagrams/                         # Generierte Diagramme (werden zur Laufzeit befüllt)
```

### Designprinzipien

Die Gedächtnisarchitektur folgt mehreren bewussten Designentscheidungen:

1. **SQLite statt Cloud-Speicher**: Das Gedächtnis ist lokal, portabel und erfordert keinerlei Infrastruktur. Die Datenbankdatei kann in das Repository eingecheckt oder zwischen Teammitgliedern geteilt werden.

2. **Konfidenzwerte statt binärer Wahrheit**: Wissen ist nicht einfach „bekannt" oder „unbekannt" — es trägt einen Konfidenzwert, der mit der Zeit abnimmt und damit die Realität widerspiegelt, dass sich Softwareprojekte weiterentwickeln und gestrige Wahrheiten heute möglicherweise nicht mehr gelten.

3. **UPSERT-Semantik**: `record_knowledge()` führt ein UPSERT durch — wenn dasselbe Tupel `(project_name, category, key)` bereits existiert, werden Wert und Konfidenz aktualisiert, anstatt einen doppelten Eintrag zu erzeugen.

4. **Trennung von Aufgabengedächtnis und Wissensdatenbank**: `task_memory` ist sitzungsbezogen und erfasst die rohen Fragen und Antworten, Entscheidungen und Ergebnisse einer einzelnen Ausführung. `knowledge_base` ist projektbezogen und erfasst destilliertes, wiederverwendbares Wissen, das über Sitzungen hinweg bestehen bleibt.

5. **WAL-Journalmodus**: Die Datenbank verwendet Write-Ahead Logging für bessere Nebenläufigkeit, wodurch Lesezugriffe während Schreibvorgängen ohne Blockierung möglich sind.

---

## Mitwirken

### Skills hinzufügen

1. Definieren Sie die Aufgabe in `task/` als Agent-Skill-Definitionsdokument.
2. Ordnen Sie die Aufgabe einer Delivery-Phase und Welle im Playbook zu.
3. Erstellen Sie das Skill-Gerüst mit `init_skill.py`.
4. Befüllen Sie alle Referenzdateien (SOP, DoR, DoD, RACI, Tools, Triggers, Output Templates).
5. Erstellen Sie den gepaarten Supervisor-Skill mit Prüfkriterien.
6. Registrieren Sie den Skill in `config/openclaw.json`.
7. Validieren Sie mit `quick_validate.py`.

### Qualitätsstandards für Skills

Jeder Skill muss Folgendes enthalten:
- Einen vollständigen Phase-0–5-SOP ohne übersprungene Phasen
- Eine DoR-Checkliste mit verifizierbaren Voraussetzungen
- Eine DoD-Checkliste mit 19 Qualitätssicherungspunkten
- Eine RACI-Matrix mit Zuordnung aller relevanten Beteiligten
- Output Templates für alle Arbeitsergebnisse
- Einen gepaarten Supervisor-Skill mit Prüfkriterien

---

## Lizenz

Dieses Projekt ist proprietär. Alle Rechte vorbehalten.
