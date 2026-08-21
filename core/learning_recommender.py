"""
=========================================================
CareerIQ Enterprise - Enterprise AI Learning Roadmap & Career Engine
Version : 12.0 Enterprise Production Edition
Author  : CareerIQ Engineering
=========================================================
"""

import os
import re
import pandas as pd
from typing import Dict, List, Any, Optional


class LearningRecommender:
    """
    Production-grade career roadmap engine that generates structured,
    phase-by-phase Zero-to-Pro learning paths for any tech role.
    """

    ROLE_ROADMAPS = {
        "AI / Machine Learning Engineer": {
            "title": "AI / Machine Learning Engineer",
            "tagline": "Master mathematical foundations, classical ML, deep neural networks, LLMs, and production MLOps.",
            "duration_weeks": 24,
            "difficulty": "Intermediate to Advanced",
            "phases": [
                {
                    "phase": "Phase 1: Mathematics & Python Mastery",
                    "duration": "Weeks 1 - 4",
                    "focus": "Python programming, Linear Algebra, Multivariable Calculus, Probability & Statistics.",
                    "topics": [
                        "Advanced Python (OOP, Generators, Type Hinting, Decorators, Asyncio)",
                        "Linear Algebra: Matrices, Eigenvalues, SVD, Dot Products",
                        "Calculus: Partial Derivatives, Gradient Descent, Backpropagation math",
                        "Statistics: Distributions, Hypothesis Testing, Bayesian Probability",
                        "Data Manipulation: NumPy arrays, Pandas DataFrames, Vectorization"
                    ],
                    "tools": ["Python 3.12+", "NumPy", "Pandas", "Matplotlib", "Seaborn", "JupyterLab"],
                    "milestone_project": "Statistical EDA & Exploratory Data Pipeline on 100K+ Real Dataset"
                },
                {
                    "phase": "Phase 2: Classical Machine Learning & Feature Engineering",
                    "duration": "Weeks 5 - 9",
                    "focus": "Supervised, Unsupervised learning, Model evaluation, and Feature engineering.",
                    "topics": [
                        "Regression (Linear, Ridge, Lasso, Polynomial)",
                        "Classification (Logistic, SVM, Decision Trees, Random Forests, XGBoost, LightGBM)",
                        "Clustering & Dim Reduction (K-Means, DBSCAN, PCA, t-SNE)",
                        "Cross-Validation, Precision-Recall, ROC-AUC, Bias-Variance Tradeoff",
                        "Scikit-learn pipelines & hyperparameter tuning (Optuna, GridSearchCV)"
                    ],
                    "tools": ["Scikit-learn", "XGBoost", "LightGBM", "Optuna", "Joblib", "SciPy"],
                    "milestone_project": "Production Fraud / Churn Prediction System with automated feature pipelines"
                },
                {
                    "phase": "Phase 3: Deep Learning & Computer Vision / NLP",
                    "duration": "Weeks 10 - 15",
                    "focus": "Neural network architectures, PyTorch, CNNs, RNNs, and Transformers.",
                    "topics": [
                        "PyTorch Deep Dive: Tensors, Autograd, Custom Datasets & Training Loops",
                        "Computer Vision: CNNs, ResNet, Transfer Learning, Object Detection (YOLO)",
                        "Natural Language Processing: Embeddings, Word2Vec, Seq2Seq, Attention Mechanisms",
                        "Transformer Architecture from Scratch: Self-Attention, Multi-Head Attention, Positional Encoding",
                        "HuggingFace Ecosystem: Transformers, Datasets, Tokenizers, Accelerate"
                    ],
                    "tools": ["PyTorch", "HuggingFace", "Torchvision", "spaCy", "TensorBoard", "Weights & Biases"],
                    "milestone_project": "Multi-Modal Document & Image Classification Engine using Fine-Tuned Transformers"
                },
                {
                    "phase": "Phase 4: Generative AI, LLMs, RAG & AI Agents",
                    "duration": "Weeks 16 - 19",
                    "focus": "Large Language Models, Retrieval-Augmented Generation, and Autonomous AI Agents.",
                    "topics": [
                        "LLM Fundamentals: Prompt Engineering, Tokenization, Context Windows, Temperature",
                        "Vector Databases & Embeddings: Pinecone, Qdrant, ChromaDB, FAISS",
                        "RAG Pipelines: Chunking strategies, Hybrid Search (Dense + Sparse BM25), Re-ranking",
                        "Fine-Tuning: LoRA, QLoRA, PEFT, Dataset curation, Evaluation benchmarks",
                        "AI Agentic Frameworks: LangChain, LlamaIndex, LangGraph, Multi-Agent Tool Calling"
                    ],
                    "tools": ["LangChain", "LlamaIndex", "LangGraph", "Ollama", "ChromaDB", "vLLM", "OpenAI / Anthropic APIs"],
                    "milestone_project": "Enterprise Agentic RAG Assistant with Memory, Tool Calling & Self-Correction"
                },
                {
                    "phase": "Phase 5: MLOps, Scalable Deployment & Cloud",
                    "duration": "Weeks 20 - 24",
                    "focus": "Model serving, Docker containerization, CI/CD, Kubernetes, and Cloud MLOps.",
                    "topics": [
                        "FastAPI Model Serving with asynchronous request batching",
                        "Containerization with Docker & Multi-stage builds",
                        "MLOps Tracking: MLflow, DVC (Data Version Control)",
                        "Cloud Deployment: AWS (EC2, Sagemaker, Lambda) / GCP (Vertex AI)",
                        "Model Monitoring: Drift detection (Evidently AI), Latency optimization (ONNX, TensorRT)"
                    ],
                    "tools": ["FastAPI", "Docker", "MLflow", "DVC", "AWS Sagemaker", "ONNX Runtime", "GitHub Actions"],
                    "milestone_project": "End-to-End Containerized MLOps Pipeline with Automated CI/CD & Model Monitoring"
                }
            ],
            "projects": [
                {
                    "tier": "Level 1: Intermediate",
                    "name": "Production Customer Churn & Fraud Predictor",
                    "stack": "Python, Scikit-learn, XGBoost, Streamlit, Docker",
                    "description": "Engineered pipeline with 92%+ precision, custom feature encoders, and live risk dashboard."
                },
                {
                    "tier": "Level 2: Advanced",
                    "name": "Fine-Tuned Specialized Medical/Legal LLM",
                    "stack": "PyTorch, HuggingFace, QLoRA, LLaMA-3, vLLM",
                    "description": "Quantized 8B model fine-tuned on domain dataset with automated evaluation metrics."
                },
                {
                    "tier": "Level 3: Production Pro Capstone",
                    "name": "Enterprise Autonomous Multi-Agent Research Platform",
                    "stack": "FastAPI, LangGraph, ChromaDB, Docker, AWS, Streamlit",
                    "description": "Agentic system with web search tools, vector retrieval, and automated PDF report generation."
                }
            ],
            "certifications": ["AWS Certified Machine Learning - Specialty", "TensorFlow Developer Certificate", "DeepLearning.AI Generative AI Specialization"],
            "resources": [
                {"name": "DeepLearning.AI (Andrew Ng)", "type": "Free/Freemium", "link": "https://www.deeplearning.ai/"},
                {"name": "Fast.ai Practical Deep Learning", "type": "100% Free", "link": "https://course.fast.ai/"},
                {"name": "Hugging Face NLP Course", "type": "100% Free", "link": "https://huggingface.co/learn/nlp-course"},
                {"name": "Full Stack Deep Learning / LLM Bootcamp", "type": "Free", "link": "https://fullstackdeeplearning.com/"}
            ]
        },
        "Data Scientist": {
            "title": "Data Scientist",
            "tagline": "Master statistics, predictive modeling, big data SQL, business analytics, and executive communication.",
            "duration_weeks": 20,
            "difficulty": "Beginner to Advanced",
            "phases": [
                {
                    "phase": "Phase 1: Statistics, Advanced SQL & Python Analytics",
                    "duration": "Weeks 1 - 4",
                    "focus": "Relational database querying, statistical hypothesis testing, and data cleaning.",
                    "topics": [
                        "Complex SQL: Window functions (ROW_NUMBER, RANK, LEAD/LAG), CTEs, Subqueries, Indexing",
                        "Statistical Foundations: Distributions, P-values, Central Limit Theorem, ANOVA, Confidence Intervals",
                        "Python Data Wrangling: Pandas groupby, pivot_tables, merge/join, handling missing values & outliers",
                        "Data Visualization: Matplotlib, Seaborn, Plotly interactive charts"
                    ],
                    "tools": ["PostgreSQL", "Python", "Pandas", "NumPy", "Plotly", "DBeaver"],
                    "milestone_project": "End-to-End E-Commerce Revenue & Cohort Retention Analytics in SQL + Python"
                },
                {
                    "phase": "Phase 2: Predictive Modeling & Experimentation (A/B Testing)",
                    "duration": "Weeks 5 - 9",
                    "focus": "Machine learning, feature engineering, and statistical experimentation.",
                    "topics": [
                        "Regression & Time Series Forecasting (ARIMA, Prophet, Exponential Smoothing)",
                        "Classification & Ensemble Methods (Random Forest, XGBoost, CatBoost)",
                        "A/B Testing Framework: Sample size calculation, Power analysis, Minimum Detectable Effect, Guardrail metrics",
                        "Feature Importance & Model Explainability (SHAP, LIME)"
                    ],
                    "tools": ["Scikit-learn", "Statsmodels", "Prophet", "SHAP", "Optuna"],
                    "milestone_project": "A/B Testing Simulation & Statistical Conversion Lift Dashboard"
                },
                {
                    "phase": "Phase 3: Business Intelligence & Executive Storytelling",
                    "duration": "Weeks 10 - 14",
                    "focus": "Power BI, Tableau, KPI design, and executive stakeholder communication.",
                    "topics": [
                        "Power BI / Tableau: Data modeling (Star Schema vs Snowflake), DAX formulas, Calculated Measures",
                        "Executive KPI Dashboard Design: Revenue run-rate, CAC, LTV, Churn, ARR tracking",
                        "Data Storytelling: Translating statistical metrics into actionable business ROI recommendations"
                    ],
                    "tools": ["Power BI", "Tableau", "DAX", "Excel Advanced", "Streamlit"],
                    "milestone_project": "Executive C-Suite KPI & Predictive Revenue Intelligence Dashboard"
                },
                {
                    "phase": "Phase 4: Big Data, Cloud & Production Pipelines",
                    "duration": "Weeks 15 - 20",
                    "focus": "Scalable big data analytics, cloud warehouses, and automated ETL pipelines.",
                    "topics": [
                        "Cloud Data Warehouses: Snowflake / Google BigQuery",
                        "Big Data Processing: PySpark (DataFrames, Spark SQL, transformations at scale)",
                        "ETL Orchestration: Apache Airflow basics, scheduled batch inference",
                        "Deploying analytics web apps with Streamlit and cloud hosting"
                    ],
                    "tools": ["PySpark", "Snowflake", "BigQuery", "Apache Airflow", "Streamlit", "AWS S3"],
                    "milestone_project": "Scalable Big Data Predictive Engine with PySpark & Cloud Warehouse Integration"
                }
            ],
            "projects": [
                {
                    "tier": "Level 1: Intermediate",
                    "name": "Customer Lifetime Value (LTV) & Churn Forecast Engine",
                    "stack": "Python, Pandas, Scikit-learn, Plotly, Streamlit",
                    "description": "Predictive model with RFM customer segmentation and SHAP feature explainability."
                },
                {
                    "tier": "Level 2: Advanced",
                    "name": "Enterprise Marketing A/B Test Decision Platform",
                    "stack": "Python, Statsmodels, SciPy, Streamlit, PostgreSQL",
                    "description": "Statistical significance calculator with Bayesian vs Frequentist hypothesis engine."
                },
                {
                    "tier": "Level 3: Production Pro Capstone",
                    "name": "Big Data PySpark & Snowflake Sales Forecasting Pipeline",
                    "stack": "PySpark, Snowflake, Prophet, Airflow, Power BI",
                    "description": "Automated ETL and time-series forecasting across 1M+ transaction records."
                }
            ],
            "certifications": ["Google Professional Data Scientist", "Microsoft Certified: Azure Data Scientist Associate", "Databricks Certified Associate Developer for Apache Spark"],
            "resources": [
                {"name": "Kaggle Learn & Micro-Courses", "type": "100% Free", "link": "https://www.kaggle.com/learn"},
                {"name": "StatQuest with Josh Starmer", "type": "Free YouTube", "link": "https://www.youtube.com/@statquest"},
                {"name": "Mode Analytics SQL Tutorial", "type": "100% Free", "link": "https://mode.com/sql-tutorial/"},
                {"name": "DataCamp / Coursera Data Science Specialization", "type": "Freemium", "link": "https://www.coursera.org/"}
            ]
        },
        "Full Stack Developer": {
            "title": "Full Stack Developer (MERN / Next.js / Python)",
            "tagline": "Build modern responsive frontends, high-performance REST/GraphQL backends, secure auth, and scalable cloud deployments.",
            "duration_weeks": 20,
            "difficulty": "Beginner to Advanced",
            "phases": [
                {
                    "phase": "Phase 1: Modern Web Core (HTML5, Modern CSS, TypeScript)",
                    "duration": "Weeks 1 - 4",
                    "focus": "Semantic HTML, responsive CSS layouts, modern JavaScript ES6+, and TypeScript fundamentals.",
                    "topics": [
                        "HTML5 Semantic Structure, SEO Best Practices, Web Accessibility (a11y)",
                        "CSS Grid, Flexbox, Custom Properties, Responsive Breakpoints, Tailwind CSS",
                        "JavaScript ES6+: Closures, Event Loop, Promises, Async/Await, DOM manipulation",
                        "TypeScript: Types, Interfaces, Generics, Union Types, Utility Types"
                    ],
                    "tools": ["HTML5", "CSS3", "Tailwind CSS", "JavaScript ES6+", "TypeScript", "VS Code"],
                    "milestone_project": "Responsive Component Design System & Interactive Dashboard in TypeScript + Tailwind"
                },
                {
                    "phase": "Phase 2: Frontend Architecture with React & Next.js",
                    "duration": "Weeks 5 - 9",
                    "focus": "Component lifecycle, state management, routing, server components, and performance optimization.",
                    "topics": [
                        "React Core: Hooks (useState, useEffect, useMemo, useCallback, useRef, custom hooks)",
                        "State Management: Zustand / Redux Toolkit, React Query (TanStack Query) for server state",
                        "Next.js App Router: Server Components (RSC), Client Components, Server Actions, Dynamic Routing",
                        "Authentication on Frontend: JWT handling, NextAuth / Supabase Auth",
                        "Performance: Lazy loading, Core Web Vitals optimization, code splitting"
                    ],
                    "tools": ["React 19", "Next.js 14+", "Zustand", "TanStack Query", "Framer Motion", "Shadcn UI"],
                    "milestone_project": "Full-Featured SaaS Product Frontend with Next.js App Router, SSR & Dark Mode"
                },
                {
                    "phase": "Phase 3: Backend Services, API Design & Databases",
                    "duration": "Weeks 10 - 15",
                    "focus": "Node.js/Express or FastAPI, RESTful APIs, database design, indexing, and security.",
                    "topics": [
                        "Node.js (Express/NestJS) or Python (FastAPI): Routing, Middleware, Validation (Zod / Pydantic)",
                        "Relational Databases: PostgreSQL, Prisma ORM / SQLAlchemy, Migration workflows, Indexing",
                        "NoSQL Databases: MongoDB / Redis for caching and session stores",
                        "API Security: JWT, OAuth2, Rate limiting, CORS, Input sanitization, Helmet",
                        "Real-Time Web: WebSockets (Socket.io) / Server-Sent Events (SSE)"
                    ],
                    "tools": ["Node.js", "Express.js", "FastAPI", "PostgreSQL", "Prisma ORM", "Redis", "MongoDB"],
                    "milestone_project": "Multi-Tenant RESTful & Real-Time API Backend with OAuth2, PostgreSQL & Redis Caching"
                },
                {
                    "phase": "Phase 4: Full Stack Integration, DevOps & Cloud Deployment",
                    "duration": "Weeks 16 - 20",
                    "focus": "Containerization, automated CI/CD pipelines, cloud deployment, and system monitoring.",
                    "topics": [
                        "Docker: Multi-stage Dockerfiles, Docker Compose for local full-stack dev",
                        "CI/CD: GitHub Actions for automated linting, testing, and deployment",
                        "Cloud Hosting: Vercel for Next.js, Render / AWS EC2 / Railway for Backend APIs, Supabase / Neon for DB",
                        "Testing: Unit & Integration tests (Vitest / Jest, Playwright / Cypress for E2E)"
                    ],
                    "tools": ["Docker", "Docker Compose", "GitHub Actions", "AWS / Vercel", "Playwright", "Supabase"],
                    "milestone_project": "Production-Grade Full-Stack SaaS Application with Payment Gateway, Auth & Cloud CI/CD"
                }
            ],
            "projects": [
                {
                    "tier": "Level 1: Intermediate",
                    "name": "Collaborative Task & Project Management App",
                    "stack": "Next.js, TypeScript, Tailwind CSS, Prisma, PostgreSQL",
                    "description": "Kanban board with drag-and-drop, optimistic UI updates, and team permissions."
                },
                {
                    "tier": "Level 2: Advanced",
                    "name": "Real-Time Chat & Video Collaboration Platform",
                    "stack": "React, Node.js, WebSockets, Redis, PostgreSQL, WebRTC",
                    "description": "Instant messaging, online presence indicators, and peer-to-peer video rooms."
                },
                {
                    "tier": "Level 3: Production Pro Capstone",
                    "name": "Full-Stack AI-Powered SaaS with Stripe Subscriptions",
                    "stack": "Next.js 14, FastAPI, PostgreSQL, Redis, Stripe, Docker, AWS",
                    "description": "Multi-tenant architecture with auth, webhook handlers, tiered billing, and AI API endpoints."
                }
            ],
            "certifications": ["Meta Front-End Developer Certificate", "AWS Certified Developer - Associate"],
            "resources": [
                {"name": "The Odin Project (Full Stack Path)", "type": "100% Free", "link": "https://www.theodinproject.com/"},
                {"name": "FullStackOpen (University of Helsinki)", "type": "100% Free", "link": "https://fullstackopen.com/"},
                {"name": "JavaScript.info", "type": "100% Free Guide", "link": "https://javascript.info/"},
                {"name": "Next.js Official Interactive Tutorial", "type": "100% Free", "link": "https://nextjs.org/learn"}
            ]
        },
        "DevOps / Cloud Engineer": {
            "title": "DevOps / Cloud & Site Reliability Engineer",
            "tagline": "Master Linux administration, Docker, Kubernetes orchestration, Terraform IaC, multi-stage CI/CD, and cloud architectures.",
            "duration_weeks": 22,
            "difficulty": "Intermediate to Advanced",
            "phases": [
                {
                    "phase": "Phase 1: Linux Administration, Bash Scripting & Networking",
                    "duration": "Weeks 1 - 4",
                    "focus": "Operating system fundamentals, shell scripting, networking, and Git workflows.",
                    "topics": [
                        "Linux OS: Process management, File systems, Permissions (chmod/chown), Systemd services",
                        "Bash Scripting: Automated backup scripts, log parsers, environment variable management",
                        "Networking Fundamentals: TCP/IP, DNS, HTTP/HTTPS, SSL/TLS certificates, SSH keys, Firewalls",
                        "Git & Version Control: Branching strategies (GitFlow, Trunk-based), Submodules, Rebasing"
                    ],
                    "tools": ["Ubuntu Linux", "Bash", "SSH", "Nginx", "Git", "Curl / Netcat"],
                    "milestone_project": "Automated Linux Server Provisioning & Nginx Reverse Proxy with SSL Certificates"
                },
                {
                    "phase": "Phase 2: Containerization & Cluster Orchestration (Docker & Kubernetes)",
                    "duration": "Weeks 5 - 10",
                    "focus": "Docker containerization, multi-stage builds, and Kubernetes orchestration.",
                    "topics": [
                        "Docker: Multi-stage Dockerfiles, caching layers, container security, Docker Compose",
                        "Kubernetes Core: Pods, Deployments, Services (ClusterIP, NodePort, LoadBalancer), Namespaces",
                        "K8s Advanced: ConfigMaps, Secrets, Persistent Volumes, Ingress Controllers (NGINX Ingress)",
                        "Helm: Writing custom Helm charts, release management, templating"
                    ],
                    "tools": ["Docker", "Kubernetes (Minikube / Kind / K3s)", "Helm", "K9s", "kubectl"],
                    "milestone_project": "High-Availability Microservices Cluster Deployed on Kubernetes with Helm & Ingress"
                },
                {
                    "phase": "Phase 3: Infrastructure as Code (IaC) & Cloud Architecture (AWS)",
                    "duration": "Weeks 11 - 16",
                    "focus": "Terraform, Ansible, AWS core cloud services, and security IAM policies.",
                    "topics": [
                        "Terraform: HCL syntax, State management, Remote backends (S3 + DynamoDB locking), Modules",
                        "AWS Core Services: VPC (Public/Private subnets, NAT Gateway), EC2, Auto-Scaling, ALB, S3, RDS, IAM",
                        "Configuration Management: Ansible playbooks for automated server configuration",
                        "Cloud Security: Principle of least privilege, Security groups, AWS Secrets Manager"
                    ],
                    "tools": ["Terraform", "Ansible", "AWS CLI", "AWS VPC / EC2 / RDS / EKS", "LocalStack"],
                    "milestone_project": "Production AWS VPC & Multi-Tier Infrastructure Provisioned 100% via Terraform"
                },
                {
                    "phase": "Phase 4: Zero-Downtime CI/CD Pipelines & Observability",
                    "duration": "Weeks 17 - 22",
                    "focus": "Continuous Integration/Continuous Deployment, monitoring, metrics, and incident alerting.",
                    "topics": [
                        "CI/CD with GitHub Actions / GitLab CI: Automated test pipelines, linting, image build & push to ECR/DockerHub",
                        "Deployment Strategies: Rolling updates, Blue-Green deployments, Canary releases with ArgoCD (GitOps)",
                        "Observability: Prometheus metrics collection, Grafana custom dashboards, Alertmanager",
                        "Log Aggregation: Loki / ELK Stack (Elasticsearch, Logstash, Kibana) for centralized log tracing"
                    ],
                    "tools": ["GitHub Actions", "ArgoCD", "Prometheus", "Grafana", "Loki", "Trivy (Security Scanner)"],
                    "milestone_project": "End-to-End GitOps CI/CD Pipeline with ArgoCD, Prometheus Monitoring & Slack Alerts"
                }
            ],
            "projects": [
                {
                    "tier": "Level 1: Intermediate",
                    "name": "Dockerized Microservice Stack with Automated GitHub Actions",
                    "stack": "Docker, GitHub Actions, Docker Hub, AWS EC2",
                    "description": "Automated build, security scan with Trivy, and continuous deployment on commit."
                },
                {
                    "tier": "Level 2: Advanced",
                    "name": "Terraform Multi-Environment AWS Cloud Architecture",
                    "stack": "Terraform, AWS (VPC, EKS, RDS, S3), Terraform Cloud",
                    "description": "Modular IaC setup provisioning staging and production environments with remote state locking."
                },
                {
                    "tier": "Level 3: Production Pro Capstone",
                    "name": "Enterprise GitOps Kubernetes Cluster with Full Observability",
                    "stack": "Kubernetes (EKS), ArgoCD, Prometheus, Grafana, Helm, Terraform",
                    "description": "Self-healing Kubernetes cluster managed by GitOps with automated Grafana SLO monitoring."
                }
            ],
            "certifications": ["AWS Certified Solutions Architect - Associate", "Certified Kubernetes Administrator (CKA)", "HashiCorp Certified: Terraform Associate"],
            "resources": [
                {"name": "DevOps Roadmap (roadmap.sh)", "type": "100% Free Guide", "link": "https://roadmap.sh/devops"},
                {"name": "Nana Janashia TechWorld with Nana", "type": "Free YouTube", "link": "https://www.youtube.com/@TechWorldwithNana"},
                {"name": "Kubernetes Official Interactive Labs", "type": "100% Free", "link": "https://kubernetes.io/docs/tutorials/"},
                {"name": "Learn Terraform (HashiCorp Tutorials)", "type": "100% Free", "link": "https://developer.hashicorp.com/terraform/tutorials"}
            ]
        },
        "Java / Backend Software Engineer": {
            "title": "Java / Backend Software Engineer",
            "tagline": "Master Core Java, Spring Boot microservices, Kafka event streaming, database indexing, and enterprise system design.",
            "duration_weeks": 20,
            "difficulty": "Beginner to Advanced",
            "phases": [
                {
                    "phase": "Phase 1: Core Java 21+, OOP & Data Structures & Algorithms",
                    "duration": "Weeks 1 - 4",
                    "focus": "Object-oriented design, Collections Framework, Multithreading, and core DSA.",
                    "topics": [
                        "Java 21+ features: Records, Pattern Matching, Virtual Threads (Project Loom), Streams API",
                        "Object-Oriented Programming: SOLID principles, Design Patterns (Factory, Singleton, Builder, Strategy)",
                        "Collections & Generics: List, Set, Map implementations, internal HashMap hashing mechanism",
                        "Data Structures & Algorithms: Arrays, Linked Lists, Trees, Graphs, Sorting, Binary Search, Dynamic Programming"
                    ],
                    "tools": ["Java 21", "IntelliJ IDEA", "Maven", "Gradle", "JUnit 5", "Mockito"],
                    "milestone_project": "High-Throughput Multithreaded In-Memory Order Book / Cache System in Core Java"
                },
                {
                    "phase": "Phase 2: Spring Boot Microservices, REST APIs & Persistence",
                    "duration": "Weeks 5 - 9",
                    "focus": "Spring Framework ecosystem, dependency injection, JPA/Hibernate, and relational databases.",
                    "topics": [
                        "Spring Core & Spring Boot 3: Inversion of Control (IoC), Dependency Injection (DI), Spring Beans",
                        "RESTful API Design: Controllers, DTOs, Exception Handlers, Bean Validation, OpenAPI / Swagger",
                        "Spring Data JPA & Hibernate: Entity relationships (@OneToMany, @ManyToMany), N+1 query problem, Caching (L1/L2)",
                        "Database Performance: SQL indexing (B-Tree), query optimization, connection pooling (HikariCP)"
                    ],
                    "tools": ["Spring Boot 3", "Spring Data JPA", "PostgreSQL / MySQL", "Hibernate", "Swagger / OpenAPI"],
                    "milestone_project": "Production E-Commerce / Banking REST API with Spring Boot, PostgreSQL & JWT Auth"
                },
                {
                    "phase": "Phase 3: Event-Driven Microservices, Kafka & Distributed Caching",
                    "duration": "Weeks 10 - 15",
                    "focus": "Asynchronous messaging, Apache Kafka, Redis distributed caching, and microservice patterns.",
                    "topics": [
                        "Microservice Patterns: API Gateway (Spring Cloud Gateway), Service Discovery (Eureka / Consul), Circuit Breaker (Resilience4j)",
                        "Apache Kafka: Producers, Consumers, Consumer Groups, Partitions, Offset Management, Idempotent Processing",
                        "Distributed Caching: Redis Cache-Aside pattern, Cache Invalidation, TTLs, Distributed Locks (Redisson)",
                        "Enterprise Security: Spring Security 6, OAuth2 / Keycloak Integration, Role-Based Access Control (RBAC)"
                    ],
                    "tools": ["Apache Kafka", "Redis", "Resilience4j", "Spring Cloud", "Keycloak", "Docker"],
                    "milestone_project": "Event-Driven Microservices Architecture with Kafka Message Queues & Redis Caching"
                },
                {
                    "phase": "Phase 4: System Design, Observability & Cloud Deployment",
                    "duration": "Weeks 16 - 20",
                    "focus": "High-level system design, distributed tracing, metrics, and Dockerized deployment.",
                    "topics": [
                        "System Design: Scalability, Load balancing, Database sharding/partitioning, CAP Theorem, Rate limiters",
                        "Observability: Micrometer, Prometheus, Grafana, OpenTelemetry & Zipkin/Jaeger distributed tracing",
                        "Testing: Automated Unit & Integration testing with Testcontainers and Mockito (90%+ code coverage)",
                        "Containerized Cloud Deployment: Docker multi-stage builds, Kubernetes deployment manifests"
                    ],
                    "tools": ["Testcontainers", "OpenTelemetry", "Zipkin", "Prometheus", "Grafana", "Docker"],
                    "milestone_project": "Distributed Enterprise Transaction System with Distributed Tracing & High Availability"
                }
            ],
            "projects": [
                {
                    "tier": "Level 1: Intermediate",
                    "name": "Spring Boot Secure Financial Transaction Service",
                    "stack": "Java 21, Spring Boot, PostgreSQL, Spring Security, JWT, JUnit 5",
                    "description": "ACID compliant banking ledger with transaction isolation and automated test suite."
                },
                {
                    "tier": "Level 2: Advanced",
                    "name": "Real-Time Event-Driven Order Processing Engine",
                    "stack": "Spring Boot, Apache Kafka, Redis, PostgreSQL, Docker",
                    "description": "Asynchronous microservices communicating over Kafka topics with sub-100ms processing latency."
                },
                {
                    "tier": "Level 3: Production Pro Capstone",
                    "name": "Enterprise Microservices Suite with API Gateway & Distributed Tracing",
                    "stack": "Spring Cloud, Kafka, Redis, Keycloak, OpenTelemetry, Docker, AWS",
                    "description": "5-microservice distributed architecture with centralized auth, circuit breakers, and Zipkin tracing."
                }
            ],
            "certifications": ["Oracle Certified Professional: Java SE Developer", "Spring Certified Professional", "AWS Certified Developer - Associate"],
            "resources": [
                {"name": "Baeldung Spring & Java Tutorials", "type": "100% Free", "link": "https://www.baeldung.com/"},
                {"name": "Java Brains (Koushik Kothagal)", "type": "Free YouTube", "link": "https://www.youtube.com/@JavaBrainsChannel"},
                {"name": "Hyperskill / JetBrains Academy Java Track", "type": "Freemium", "link": "https://hyperskill.org/"},
                {"name": "System Design Primer (GitHub)", "type": "100% Free Guide", "link": "https://github.com/donnemartin/system-design-primer"}
            ]
        },
        "Cybersecurity / Security Analyst": {
            "title": "Cybersecurity / Information Security Analyst",
            "tagline": "Master network defense, penetration testing, SIEM SOC log analysis, OWASP web application security, and incident response.",
            "duration_weeks": 20,
            "difficulty": "Beginner to Advanced",
            "phases": [
                {
                    "phase": "Phase 1: Computer Networking & Linux Fundamentals",
                    "duration": "Weeks 1 - 4",
                    "focus": "TCP/IP models, packet analysis, Wireshark, Linux administration, and security scripting.",
                    "topics": [
                        "Networking: OSI & TCP/IP models, DNS, DHCP, Subnetting, Routing protocols, Firewalls, VPNs",
                        "Packet Analysis: Wireshark deep packet inspection, TCP handshakes, protocol anomalies",
                        "Linux Security: Kali Linux / Ubuntu, permission hardening, bash & Python scripting for security tasks"
                    ],
                    "tools": ["Wireshark", "Kali Linux", "Bash", "Python", "Nmap", "Netcat"],
                    "milestone_project": "Network Reconnaissance & Vulnerability Scanning Audit with Nmap & Python"
                },
                {
                    "phase": "Phase 2: Web Application Security & Penetration Testing",
                    "duration": "Weeks 5 - 9",
                    "focus": "OWASP Top 10 vulnerabilities, Burp Suite, exploitation techniques, and secure coding.",
                    "topics": [
                        "OWASP Top 10: SQL Injection (SQLi), Cross-Site Scripting (XSS), CSRF, IDOR, SSRF, Broken Auth",
                        "Web Proxy & Testing: Burp Suite Professional/Community, intercepting and tampering HTTP requests",
                        "Penetration Testing Methodology: Reconnaissance, Enumeration, Exploitation, Privilege Escalation"
                    ],
                    "tools": ["Burp Suite", "OWASP ZAP", "Metasploit", "SQLmap", "Gobuster"],
                    "milestone_project": "Comprehensive Web Application Penetration Test & Remediation Audit Report"
                },
                {
                    "phase": "Phase 3: SOC Operations, SIEM & Threat Hunting",
                    "duration": "Weeks 10 - 15",
                    "focus": "Security Operations Center (SOC) workflows, SIEM rule authoring, log analysis, and incident detection.",
                    "topics": [
                        "SIEM Platforms: Splunk / Elastic Security / Microsoft Sentinel log aggregation and search syntax",
                        "Threat Detection: Writing correlation rules for brute-force attacks, ransomware, and abnormal data egress",
                        "MITRE ATT&CK Framework: Mapping attacker Tactics, Techniques, and Procedures (TTPs)",
                        "Incident Response: SANS Incident Handling steps (Identification, Containment, Eradication, Recovery)"
                    ],
                    "tools": ["Splunk", "Elasticsearch / Kibana", "Sysmon", "Wazuh", "YARA", "Snort / Suricata"],
                    "milestone_project": "Automated SIEM SOC Threat Detection & Incident Response Playbook on Wazuh/Splunk"
                },
                {
                    "phase": "Phase 4: Cloud Security, Cryptography & Compliance",
                    "duration": "Weeks 16 - 20",
                    "focus": "AWS/Azure cloud security posture, IAM least privilege, encryption standards, and compliance frameworks.",
                    "topics": [
                        "Cloud Security: AWS IAM hardening, GuardDuty, Security Hub, S3 bucket policy audits",
                        "Applied Cryptography: Symmetric (AES), Asymmetric (RSA/ECC), Hashing (SHA-256), PKI & SSL/TLS",
                        "Compliance & Frameworks: ISO 27001, SOC 2, NIST Cybersecurity Framework, GDPR"
                    ],
                    "tools": ["AWS IAM", "ScoutSuite", "OpenSSL", "Trivy", "CloudTrail"],
                    "milestone_project": "Multi-Cloud Security Posture Assessment & Automated Compliance Audit Pipeline"
                }
            ],
            "projects": [
                {
                    "tier": "Level 1: Intermediate",
                    "name": "Automated Network Vulnerability & Port Scanner in Python",
                    "stack": "Python, Socket, Scapy, Nmap, SQLite",
                    "description": "Custom scanner identifying open ports, banners, and outdated software vulnerabilities."
                },
                {
                    "tier": "Level 2: Advanced",
                    "name": "Full OWASP Web Application Penetration Audit",
                    "stack": "Burp Suite, OWASP ZAP, Kali Linux, Python",
                    "description": "Discovered and remediated 5 high-severity vulnerabilities on a staging web platform."
                },
                {
                    "tier": "Level 3: Production Pro Capstone",
                    "name": "Enterprise Wazuh / Splunk SOC Monitoring & Automated Playbook",
                    "stack": "Wazuh SIEM, Splunk, Suricata IDS, Python, Docker",
                    "description": "Configured real-time threat detection rules with automated IP blocking and Slack alerts."
                }
            ],
            "certifications": ["CompTIA Security+ (SY0-701)", "Certified Ethical Hacker (CEH)", "Certified Information Systems Security Professional (CISSP / Associate)"],
            "resources": [
                {"name": "TryHackMe (Hands-on Rooms)", "type": "Freemium", "link": "https://tryhackme.com/"},
                {"name": "Hack The Box (Penetration Labs)", "type": "Freemium", "link": "https://www.hackthebox.com/"},
                {"name": "Professor Messer Security+ Training", "type": "100% Free YouTube", "link": "https://www.professormesser.com/"},
                {"name": "OWASP Official Documentation", "type": "100% Free", "link": "https://owasp.org/"}
            ]
        }
    }

    def __init__(self):
        path = "data/learning_paths.csv"
        if os.path.exists(path):
            self.learning = pd.read_csv(path)
        else:
            self.learning = pd.DataFrame(columns=["Skill", "Difficulty", "Duration", "Course", "Project"])

    def get_supported_roles(self) -> List[str]:
        """
        Returns list of rich pre-configured role roadmaps.
        """
        return list(self.ROLE_ROADMAPS.keys())

    def generate_custom_roadmap_for_role(
        self,
        role_name: str,
        current_level: str = "Beginner / Fresher",
        timeline_weeks: int = 24
    ) -> Dict[str, Any]:
        """
        Generates a tailored, comprehensive 5-phase learning roadmap for ANY entered role.
        """
        role_name_clean = role_name.strip().title()

        # Check if we have an exact or close match in pre-built roadmaps
        for preset_role, data in self.ROLE_ROADMAPS.items():
            if preset_role.lower() in role_name_clean.lower() or role_name_clean.lower() in preset_role.lower():
                # Adjust duration based on user timeline choice
                adjusted_data = dict(data)
                adjusted_data["selected_level"] = current_level
                adjusted_data["duration_weeks"] = timeline_weeks
                return adjusted_data

        # Dynamic AI Generator for any custom role entered by user
        # Parse technical keywords from role name
        role_tokens = [w for w in re.split(r"[\s\/\-\_]+", role_name_clean) if len(w) >= 3]
        primary_tech = role_tokens[0] if role_tokens else "Core Technologies"

        phases = [
            {
                "phase": f"Phase 1: Foundations & Core Principles of {role_name_clean}",
                "duration": f"Weeks 1 - {max(3, timeline_weeks // 5)}",
                "focus": f"Master foundational programming, math, design patterns, and basic tooling for {role_name_clean}.",
                "topics": [
                    f"Core programming languages and runtime environments relevant to {role_name_clean}",
                    "Data Structures, Algorithms, and clean code principles",
                    "Version Control with Git, GitHub branching, and code collaboration",
                    "Fundamental architecture concepts and developer environment setup"
                ],
                "tools": ["Git", "VS Code", "Terminal / Bash", f"{primary_tech} Core Tools"],
                "milestone_project": f"Foundational {role_name_clean} Project demonstrating core algorithms and clean architecture"
            },
            {
                "phase": f"Phase 2: Core Engineering & Industry Frameworks",
                "duration": f"Weeks {timeline_weeks // 5 + 1} - {max(timeline_weeks // 5 * 2, 7)}",
                "focus": f"Deep dive into standard industry frameworks, libraries, and protocols for {role_name_clean}.",
                "topics": [
                    f"Specialized frameworks and toolkits utilized by professional {role_name_clean}s",
                    "Database modeling, state management, and reliable data persistence",
                    "API design, client-server communication, and security best practices",
                    "Unit testing, integration testing, and debugging workflows"
                ],
                "tools": [f"{primary_tech} Frameworks", "SQL / NoSQL Databases", "Postman / Testing Tools", "Docker"],
                "milestone_project": f"Comprehensive {role_name_clean} Application with complete database integration"
            },
            {
                "phase": f"Phase 3: Advanced Systems, Performance & Scalability",
                "duration": f"Weeks {timeline_weeks // 5 * 2 + 1} - {max(timeline_weeks // 5 * 3, 12)}",
                "focus": "Performance tuning, distributed caching, security hardening, and resilient architectures.",
                "topics": [
                    "High-performance execution, memory management, and asynchronous operations",
                    "System design principles: Scalability, Caching, Load Balancing, Fault Tolerance",
                    "Security hardening: Authentication, Authorization, Input sanitization, Data encryption",
                    "Code profiling, bottleneck identification, and optimization strategies"
                ],
                "tools": ["Redis / Caching", "Docker", "Monitoring Tools", "Profiling Suites"],
                "milestone_project": f"High-Performance Resilient {role_name_clean} System with Caching & Security"
            },
            {
                "phase": f"Phase 4: Production Deployment, Cloud & Automation (DevOps)",
                "duration": f"Weeks {timeline_weeks // 5 * 3 + 1} - {max(timeline_weeks // 5 * 4, 18)}",
                "focus": "Containerization, automated CI/CD pipelines, cloud hosting, and real-time monitoring.",
                "topics": [
                    "Containerization with Docker and container registries",
                    "Automated CI/CD workflows using GitHub Actions / GitLab CI",
                    "Cloud deployment (AWS / GCP / Azure) and infrastructure management",
                    "Application telemetry, logging, and automated error alerting"
                ],
                "tools": ["Docker", "GitHub Actions", "AWS / Cloud Platforms", "Prometheus / Grafana"],
                "milestone_project": f"Production-Grade Cloud-Deployed {role_name_clean} Architecture with CI/CD"
            },
            {
                "phase": "Phase 5: Portfolio Polish, Interview Mastery & Pro Hiring Strategy",
                "duration": f"Weeks {timeline_weeks // 5 * 4 + 1} - {timeline_weeks}",
                "focus": "Interview preparation, live coding problem solving, GitHub showcase, and resume positioning.",
                "topics": [
                    f"Technical Interview Questions & Scenario-based problem solving for {role_name_clean}",
                    "System Design and Architecture whiteboard interview drills",
                    "GitHub Portfolio curation with comprehensive READMEs and live demo links",
                    "LinkedIn & Resume optimization targeting senior recruiter search keywords"
                ],
                "tools": ["LeetCode / HackerRank", "GitHub", "LinkedIn Recruiter", "Portfolio Demo Platforms"],
                "milestone_project": f"Enterprise Capstone Showcase & Live Portfolio demonstrating end-to-end {role_name_clean} mastery"
            }
        ]

        return {
            "title": role_name_clean,
            "tagline": f"Comprehensive Zero-to-Pro roadmap tailored to master {role_name_clean} and land high-paying engineering roles.",
            "duration_weeks": timeline_weeks,
            "difficulty": "Custom Tailored Path",
            "selected_level": current_level,
            "phases": phases,
            "projects": [
                {
                    "tier": "Level 1: Intermediate",
                    "name": f"Foundational {role_name_clean} Core Application",
                    "stack": f"{primary_tech}, Modern Libraries, Clean Architecture, Git",
                    "description": "Well-architected system demonstrating core domain fundamentals and clean code."
                },
                {
                    "tier": "Level 2: Advanced",
                    "name": f"Full-Featured {role_name_clean} Platform with Real-Time Data",
                    "stack": f"{primary_tech}, SQL Database, Redis Caching, Docker",
                    "description": "Production-grade system with user authentication, database persistence, and optimization."
                },
                {
                    "tier": "Level 3: Production Pro Capstone",
                    "name": f"Enterprise Scalable {role_name_clean} Infrastructure",
                    "stack": f"{primary_tech}, Cloud (AWS), Docker, GitHub Actions CI/CD",
                    "description": "Multi-tier cloud deployment with automated testing, monitoring, and live public URL."
                }
            ],
            "certifications": [f"Industry Standard Certification for {role_name_clean}", "AWS Certified Solutions Architect", "Professional Domain Certificate"],
            "resources": [
                {"name": f"Official {role_name_clean} Documentation & Standards", "type": "100% Free", "link": "https://developer.mozilla.org/"},
                {"name": "Roadmap.sh Community Developer Guides", "type": "100% Free", "link": "https://roadmap.sh/"},
                {"name": "FreeCodeCamp & MIT OpenCourseWare", "type": "100% Free", "link": "https://www.freecodecamp.org/"},
                {"name": "Coursera / edX Technical Specializations", "type": "Freemium", "link": "https://www.coursera.org/"}
            ]
        }

    def generate_export_text(self, roadmap_data: Dict[str, Any]) -> str:
        """
        Generates a comprehensive text document of the complete learning roadmap.
        """
        title = roadmap_data.get("title", "Software Engineer")
        duration = roadmap_data.get("duration_weeks", 24)
        difficulty = roadmap_data.get("difficulty", "Intermediate")

        text = f"""================================================================================
CareerIQ - ZERO-TO-PRO CAREER & LEARNING ROADMAP
Target Role : {title}
Timeline    : {duration} Weeks
Level       : {roadmap_data.get('selected_level', 'All Levels')} ({difficulty})
================================================================================

OVERVIEW:
{roadmap_data.get('tagline', '')}

================================================================================
PHASE-BY-PHASE MASTERY ROADMAP
================================================================================
"""
        for p in roadmap_data.get("phases", []):
            text += f"\n--------------------------------------------------------------------------------\n"
            text += f"📌 {p['phase']} ({p['duration']})\n"
            text += f"Focus: {p['focus']}\n\n"
            text += f"Key Topics to Master:\n"
            for t in p.get("topics", []):
                text += f"  • {t}\n"
            text += f"\nEssential Tools: {', '.join(p.get('tools', []))}\n"
            text += f"Milestone Project: {p.get('milestone_project', 'N/A')}\n"

        text += f"""
================================================================================
RESUME-READY INDUSTRY PROJECT BLUEPRINTS
================================================================================
"""
        for prj in roadmap_data.get("projects", []):
            text += f"\n[{prj['tier']}] {prj['name']}\n"
            text += f"Tech Stack  : {prj['stack']}\n"
            text += f"Description : {prj['description']}\n"

        text += f"""
================================================================================
RECOMMENDED CERTIFICATIONS & LEARNING RESOURCES
================================================================================
Target Certifications:
"""
        for cert in roadmap_data.get("certifications", []):
            text += f"  ✓ {cert}\n"

        text += f"\nTop Curated Resources:\n"
        for r in roadmap_data.get("resources", []):
            text += f"  • {r['name']} ({r['type']}) - {r['link']}\n"

        text += """
================================================================================
Generated by CareerIQ Enterprise Talent Intelligence Platform
================================================================================
"""
        return text