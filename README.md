# Backend project
Структура Обучения

📂 Oleg14038backend/
│
├── py-basics-labs/           # 🧩 основа Python (01–13)
│   ├── basics/
│   ├── docs/
│   ├── tests/
│   └── requirements.txt
│
├── python-sql-labs/          # 🧮 SQL и ORM (SQLite, SQLAlchemy, Alembic)
│   ├── sql_raw/              # чистый SQL
│   ├── sqlalchemy_basics/
│   ├── alembic_migrations/
│   └── tests/
│
├── security-labs/            # 🔐 хеши, JWT, токены, авторизация
│   ├── hashing/
│   ├── jwt_tokens/
│   ├── crypto_basics/
│   └── tests/
│
├── billing-labs/             # 💼 инвойсы, CSV, Excel, PDF
│   ├── csv_excel/
│   ├── pdf_reports/
│   ├── invoice_examples/
│   └── tests/
│
├── backend-FastAPI/          # ⚡ API сервер
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── db/
│   │   ├── core/
│   │   └── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── backend-Django/           # 🧱 Django backend (ORM, admin, REST)
│   ├── core/
│   ├── apps/
│   ├── tests/
│   └── manage.py
│
└── shared-libs/              # ⚙️ общие библиотеки и утилиты (модули, логеры, helpers)   ├── logging_utils/
    ├── config_tools/
    ├── async_helpers/
    └── README.md

dev-automation-labs/
├── powershell/          # 💻 скрипты для Windows (PowerShell)
│   ├── create_repos.ps1
│   ├── setup_env.ps1
│   ├── git_tools.ps1
│   └── docker_setup.ps1
│
├── bash/                # 🐧 скрипты для Linux/macOS
│   ├── create_repos.sh
│   ├── setup_env.sh
│   └── deploy_fastapi.sh
│
├── python/              # 🐍 Python-утилиты автоматизации
│   ├── generate_structure.py
│   ├── github_issues_creator.py
│   └── dockerfile_generator.py
│
├── docs/                # 📖 твои конспекты, объяснения
│   ├── 01_git_basics.md
│   ├── 02_powershell_basics.md
│   ├── 03_automation_principles.md
│   └── README.md
│
└── README.md
