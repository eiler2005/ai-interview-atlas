# AI-лидерство: аудит покрытия и свидетельств

[English](../../research/LEADERSHIP_AUDIT.md) · [Русский](LEADERSHIP_AUDIT.md) · [Практические кейсы](../learning/AI_LEADERSHIP.md) · [Учебный план](../LEARNING_PATH.md)

Дата аудита: **05.10.2026**. **Исходный срез до исправлений содержания:** `6648af25ee5f04f1141b96a81900032af06a460d`, всего 294 вопроса. Исходные выводы и 20 проверок ниже описывают этот срез; ссылки ведут к текущим вопросам. Дополнение о текущем содержании фиксирует последующие исправления и добавления. Это аудит учебного материала, а не утверждение, что коллекция покрывает все лидерские интервью.

Все **155 вопросов с тегом Leadership** по отдельности проверены по смыслу формулировки, компетенции и чек-листа, соответствию роли/уровню, метаданным происхождения и наличию чтения и ответов. В треке **70 приоритетных вопросов Leadership** и **89 вопросов с написанным ответом**: во второе число входят общие вопросы, приоритетные только для Engineering. Чек-листы есть у всех 155; чтения нет у 37. Рабочая запись по каждому вопросу отделяет редакционную ветку от роли, названной в свидетельстве. Семантический аудит не означает свежую фактическую проверку всех 155 источников. Отдельная проверка ниже охватывает **20 разных вопросов**.

## Что поддерживает исходный банк

Для продуктового discovery, выбора AI, метрик, решений о запуске и управления инженерной командой есть пригодный учебный материал. Технические вопросы полезны и для архитектурного ревью руководителя, если упражнение требует решения, владельца эксплуатации и доказательств. Техническая сложность сама по себе не устанавливает управленческий уровень.

Подготовка Head/Director заметно слабее. Приоритизация функций, стоимость задачи, рассказ о большой команде и влияние на заинтересованных лиц — полезные предпосылки, но по отдельности не проверяют портфель с ограничениями денег и людей. Новые кейсы добавляют распределение портфеля, build/buy, управление через менеджеров и решения руководства как **редакционную практику**. Это не доказательство, что работодатели задают такие кейсы.

Для TPM есть полезные сценарии зависимостей, неопределённости и готовности. Несколько наиболее ясных сценариев сгенерированы, а вопросы со свидетельствами о доставке преимущественно происходят из PM/EM-материалов. Их учебная применимость сильнее, чем доказательство специализированных AI TPM-интервью.

### Исходный состав свидетельств

Считаем вопрос один раз по сочетанию видов свидетельств, а не по каждой атрибуции компании:

| Сочетание | Вопросов | Что подтверждает |
| --- | ---: | --- |
| Только руководство по подготовке | 31 | Вторичный подготовительный материал |
| Только компиляция | 84 | Непроверенная атрибуция вопроса из подборки |
| Руководство и компиляция | 1 | Два вида вторичного материала, не подтверждение из первых рук |
| Рассказ участника | 23 | Публичный рассказ кандидата/интервьюера в пределах указанной роли и даты |
| Официальный источник | 2 | Материал работодателя для общего PM или Senior Staff+ |
| Сгенерировано; свидетельств об интервью нет | 14 | Только редакционная практика |

Компиляция связана с 85 разными вопросами, включая смешанную строку. У многих руководств и рассказов один издатель; число источников не равно независимому подтверждению. Технический первоисточник усиливает учебную опору ответа, но не атрибуцию интервью. Вакансия описывает обязанности, а не вопрос или этап интервью. См. [методологию](../METHODOLOGY.md).

## Исходная матрица компетенций P0

Это редакционные приоритеты подготовки по ответственности, а не по названию должности или частоте на рынке. **Покрыто** — в банке есть пригодные вопрос, чек-лист и учебная опора для указанного масштаба; **частично** — отсутствует важное решение/результат; **нет** — нет прямого текущего вопроса для данного масштаба. Это оценка материала, не ученика. Сила свидетельств — отдельная колонка. **A** — написанный ответ; **O** — только чек-лист. Точный список чтения находится в каждом вопросе; названные материалы — отправные точки, а не новые свидетельства об интервью. Коды кейсов ведут в [дополнение](../learning/AI_LEADERSHIP.md).

| Компетенция P0 | Роль и масштаб | Точные вопросы; ответы и чтение | Учебное покрытие до дополнения | Ограничение свидетельств об интервью | Практика |
| --- | --- | --- | --- | --- | --- |
| Discovery и AI/без AI | Product, старший IC/lead | [prod-enterprise-discovery](../themes/ai-product-strategy.md#prod-enterprise-discovery), [prod-ai-suitability](../themes/ai-product-strategy.md#prod-ai-suitability), [prod-expensive-mvp](../themes/ai-product-strategy.md#prod-expensive-mvp): A; набор респондентов, Rules of ML | Покрыто для ограниченной возможности | Рассказ интервьюера и руководство; уровень редакционный | P1 |
| Метрики и эксперименты | Product, старший IC/lead | [prod-ai-feature-metrics](../themes/ai-product-strategy.md#prod-ai-feature-metrics): A, HEART; [eval-online](../themes/evals-observability.md#eval-online): O, оценка | Частично: нужен выполненный анализ валидности эксперимента | Руководство/компиляция; тег eval-engineer не доказывает PM-интервью | P2 |
| Экономика, доверие, запуск/остановка | Product, старший IC/lead | [prod-enterprise-ai-pricing](../themes/ai-product-strategy.md#prod-enterprise-ai-pricing), [prod-confident-errors](../themes/ai-product-strategy.md#prod-confident-errors), [prog-prelaunch-hallucinations](../themes/program-delivery.md#prog-prelaunch-hallucinations): A; экономика, NIST, оценка агентов | Покрыто для одного продукта; решения нужно объединить в практике | Интервьюер и вторичные образцы; не универсальный процесс | P3 |
| Архитектура и надёжность | EM/Platform, владелец команды/сервиса | [sd-gateway](../themes/ai-system-design.md#sd-gateway), [eval-release-gate](../themes/evals-observability.md#eval-release-gate), [inf-cost-reduction](../themes/inference-economics.md#inf-cost-reduction): A; идемпотентность, оценка, SRE | Техническое ревью покрыто; полномочия эксплуатации частично | Компиляция и инженерные теги практики | E1 |
| Разработка с AI и сигнал найма | EM/Platform, менеджер людей | [lead-ai-review-skills](../themes/engineering-leadership.md#lead-ai-review-skills): A; [lead-ai-interview-redesign](../themes/engineering-leadership.md#lead-ai-interview-redesign): O; AI-resistant evaluations | Частично: нет наблюдаемого ревью/калибровки | Сгенерировано; официальный блог — чтение, не свидетельство этих вопросов | E2 |
| Комплектование команды и владение платформой | EM/Platform, lead/менеджер | [lead-platform-team-charter](../themes/engineering-leadership.md#lead-platform-team-charter), [ops-platform-ownership](../themes/ai-operating-model.md#ops-platform-ownership), [lead-strategic-hiring](../themes/engineering-leadership.md#lead-strategic-hiring): A; Team Topologies, SRE, обучение менеджеров | Устав команды покрыт; нужен расчёт мощности | Сгенерировано и общие вторичные менеджерские материалы | E3 |
| Развитие людей, результативность и состояние команды | EM, линейный менеджер | [lead-low-performance](../themes/engineering-leadership.md#lead-low-performance), [lead-mentee-growth](../themes/engineering-leadership.md#lead-mentee-growth), [lead-team-after-change](../themes/engineering-leadership.md#lead-team-after-change): A; обучение менеджеров, оргизменения | Покрыто на уровне команды; адаптации источника отмечены ниже | Общие EM-рассказы, не доказательство AI-специализации интервью | E4 |
| Портфель и бюджет | Head/Director, делегированные права на портфель | [prod-roadmap](../themes/ai-product-strategy.md#prod-roadmap), [prod-product-cannibalisation](../themes/ai-product-strategy.md#prod-product-cannibalisation): O, без чтения; [inf-cost-reduction](../themes/inference-economics.md#inf-cost-reduction): A | **Нет прямого кейса бюджета нескольких инициатив**; вопросы — подготовка | PM/технические материалы; недостаточно director-свидетельств | H1 |
| Build/buy и ресурсы | Head/Director, владелец инвестиций | [app-open-model-engagement](../themes/applied-scenarios.md#app-open-model-engagement): O, оценка/serving; [lead-platform-team-charter](../themes/engineering-leadership.md#lead-platform-team-charter): A | Частично: нет совместной проверки выхода от поставщика, людей, альтернативных затрат и денег | Компиляция/сгенерировано; недостаточно director-свидетельств | H2 |
| Оргизменения и руководство | Head/Director, несколько команд/менеджеров | [lead-team-scale](../themes/engineering-leadership.md#lead-team-scale), [lead-reorganisation-retention](../themes/engineering-leadership.md#lead-reorganisation-retention), [beh-stakeholder-priorities](../themes/behavioral-values.md#beh-stakeholder-priorities): A; обучение менеджеров, оргизменения | Частично: нужен масштаб управления менеджерами | EM-рассказ/компиляция; director-процесс не подтверждён | H3 |
| Исследовательская неопределённость и вехи | TPM/Delivery, владелец программы | [prog-research-milestones](../themes/program-delivery.md#prog-research-milestones), [lead-research-product-boundary](../themes/engineering-leadership.md#lead-research-product-boundary): A; design docs, Rules of ML | Концептуально покрыто; нужен план опровержимых вех | Сгенерировано; нет опубликованного TPM-вопроса | T1 |
| Зависимости и восстановление графика | TPM/Delivery, несколько команд | [prog-dependency-slip](../themes/program-delivery.md#prog-dependency-slip), [prog-cross-team-delivery](../themes/program-delivery.md#prog-cross-team-delivery): A; карта зависимостей, design docs | Перепланирование покрыто | Сгенерировано и EM-рассказ; рассказ недоступен при этой проверке | T2 |
| Готовность, запуск и инциденты | TPM/Delivery, координация релиза | [prog-multi-owner-readiness](../themes/program-delivery.md#prog-multi-owner-readiness), [prog-device-update](../themes/program-delivery.md#prog-device-update), [app-pilot-rescue](../themes/applied-scenarios.md#app-pilot-rescue): A; NIST, SRE, оценка | Покрыто раздельно; нужна единая репетиция инцидента | Сгенерировано/PM-руководство/компиляция; не прямое TPM-свидетельство | T3 |
| Техническая грамотность, оценка и полномочия действий | Все четыре; глубина по ответственности | [pt-method-choice](../themes/post-training.md#pt-method-choice), [eval-benchmark-mismatch](../themes/evals-observability.md#eval-benchmark-mismatch), [sec-action-authorisation](../themes/safety-security-governance.md#sec-action-authorisation), [sec-safe-deployment](../themes/safety-security-governance.md#sec-safe-deployment): A; RAG/LoRA, Rules of ML, NIST | Решения покрыты; не заменяет инженерную реализацию | Преимущественно компиляция; учебная опора сильнее атрибуции | S1 |
| Правдивый поведенческий опыт | Все четыре; реальные права и вклад | [beh-mistake-learning](../themes/behavioral-values.md#beh-mistake-learning), [prog-initiative-retrospective](../themes/program-delivery.md#prog-initiative-retrospective): A; культура постмортемов | Метод построения рассказа покрыт | Компиляция/EM-рассказ; опыт ученика должен быть реальным | S2 |

## Исходная проверка двадцати вопросов по источникам

Все проверки выполнены **05.10.2026** по публичному содержимому. Это целевая выборка по пять учебных опор на ветку, а не случайная оценка точности. Строки Head/Director намеренно проверяют переносимые предпосылки: прямых director-свидетельств недостаточно. Строки TPM не переименовывают PM/EM-рассказы в TPM. «Совпадает» означает подтверждение сути вопроса, а не редакционного ответа и всех уточнений. Самоназвание источника «проверенным» не повышало его статус.

| Ветка | Канонический вопрос | Точный источник и открытый раздел | Результат |
| --- | --- | --- | --- |
| Product | [prod-enterprise-ai-pricing](../themes/ai-product-strategy.md#prod-enterprise-ai-pricing) | [Рассказ интервьюера на Хабре][HABR], экономика | Совпадает: цена, затраты, кастомизация; участник без указанного работодателя |
| Product | [prod-enterprise-discovery](../themes/ai-product-strategy.md#prod-enterprise-discovery) | [Хабр][HABR], discovery | Совпадает: персона, респонденты, ценность проблемы |
| Product | [prod-expensive-mvp](../themes/ai-product-strategy.md#prod-expensive-mvp) | [Хабр][HABR], прототипирование | Совпадает: дорогой/долгий MVP; чек-лист редакционный |
| Product | [prod-notification-paradox](../themes/ai-product-strategy.md#prod-notification-paradox) | [Участник Meta AI PM][META-PM], аналитический этап | Совпадает; общий аналитический вопрос в AI-PM интервью |
| Product | [prod-impactful-product](../themes/ai-product-strategy.md#prod-impactful-product) | [Monzo PM][MONZO-PM], рассказ о продукте | Совпадает; официальный **общий PM**, 2022 год |
| EM/Platform | [lead-low-performance](../themes/engineering-leadership.md#lead-low-performance) | [Участник Google L6 EM][GOOGLE-EM], управление людьми | **Адаптировано:** в источнике гипотеза, в банке прошлый опыт |
| EM/Platform | [lead-disruptive-star](../themes/engineering-leadership.md#lead-disruptive-star) | [Google L6 EM][GOOGLE-EM], управление людьми | **Адаптировано:** в источнике гипотеза, в банке прошлый опыт |
| EM/Platform | [lead-mentee-growth](../themes/engineering-leadership.md#lead-mentee-growth) | [Участник Anthropic EM][ANTHROPIC-EM], менеджерские вопросы | Совпадает; EM-рассказ, не director-подтверждение |
| EM/Platform | [lead-team-disagrees](../themes/engineering-leadership.md#lead-team-disagrees) | [Anthropic EM][ANTHROPIC-EM], менеджерские вопросы | Совпадает; способ ответа редакционный |
| EM/Platform | [lead-team-after-change](../themes/engineering-leadership.md#lead-team-after-change) | [Google L6 EM][GOOGLE-EM], моральное состояние новой команды | Совпадает по сути; банк обобщает сценарий |
| Подготовка Head/Director | [lead-team-scale](../themes/engineering-leadership.md#lead-team-scale) | [Anthropic EM][ANTHROPIC-EM], процесс и менеджерские вопросы | Совпадает для EM; управление менеджерами не установлено |
| Подготовка Head/Director | [lead-reorganisation-retention](../themes/engineering-leadership.md#lead-reorganisation-retention) | [Google L6 EM][GOOGLE-EM], сложное изменение | **Адаптировано:** в источнике фактический уход, в банке угроза ухода |
| Подготовка Head/Director | [lead-opportunity-coalition](../themes/engineering-leadership.md#lead-opportunity-coalition) | [Monzo Senior Staff+][MONZO-STAFF], влияние и лидерство | Совпадает; официальное лидерство **IC**, не director/EM интервью |
| Подготовка Head/Director | [prod-product-cannibalisation](../themes/ai-product-strategy.md#prod-product-cannibalisation) | [Meta AI PM][META-PM], уточнение marketplace-кейса | Совпадает; L5 PM, не интервью владельца портфеля |
| Подготовка Head/Director | [lead-strategic-hiring](../themes/engineering-leadership.md#lead-strategic-hiring) | [Подготовка Stripe][STRIPE], люди/организация | Частично: стратегический найм; банк переформулирует тему; вторично |
| Перенос в TPM/Delivery | [prog-difficult-launch](../themes/program-delivery.md#prog-difficult-launch) | [OpenAI PM][OPENAI-PM], вопросы о запуске | Совпадает во вторичном руководстве; масштаб PM |
| Перенос в TPM/Delivery | [prog-prelaunch-hallucinations](../themes/program-delivery.md#prog-prelaunch-hallucinations) | [Amazon AI PM][AMAZON-PM], примеры по GenAI | Совпадает с **учебным образцом**, не первичным рассказом |
| Перенос в TPM/Delivery | [prog-device-update](../themes/program-delivery.md#prog-device-update) | [Amazon AI PM][AMAZON-PM], продуктовые примеры | Совпадает; вторичное PM-руководство |
| Перенос в TPM/Delivery | [prog-cross-team-delivery](../themes/program-delivery.md#prog-cross-team-delivery) | [Meta EM][META-EM], попытка открыть исходный URL и перенаправление | **Недоступно:** публичная загрузка не удалась; проверка не пройдена |
| Перенос в TPM/Delivery | [prog-initiative-retrospective](../themes/program-delivery.md#prog-initiative-retrospective) | [Anthropic EM][ANTHROPIC-EM], презентация инициативы | Совпадает; презентация EM, не TPM-процесс |

Адаптации и частичное соответствие выше — исторические выводы об исходных формулировках, а не описание исправленных вопросов, открываемых по ссылкам. Первый проход аудита не менял банк. Последующий разрешённый проход содержания ниже согласовал четыре вопроса, сохранив ID и виды свидетельств. Гипотетическая практика и правдивый прошлый опыт остаются разными форматами.

## Дополнение о текущем содержании — 05.10.2026

После расширения в Leadership **160 вопросов, 76 приоритетов и 97 вопросов с ответами**, включая общие приоритеты Engineering. По двум трекам — **299 вопросов, 158 приоритетных вопросов с ответами, 247 источников и чтение у всех 299 вопросов**. Количества подтверждают наличие материала, а не освоение навыков или фактическую проверку. Исходная семантическая запись по 155 вопросам остаётся датированным срезом; новые и переформулированные вопросы получили отдельные проверки ниже. Двадцать исходных проверок не подтверждают все новые ответы или все текущие атрибуции работодателей.

### Исправления по первоисточнику

| Сохранённый ID | Текущая формулировка/тип и согласованные материалы | Текущий вывод по источнику |
| --- | --- | --- |
| [lead-low-performance](../themes/engineering-leadership.md#lead-low-performance) | Гипотетическая проблема результатов; тип applied scenario, будущие действия поддержки и проверки | Отчёт участника Google L6 EM перечитан; гипотетическая суть совпадает |
| [lead-disruptive-star](../themes/engineering-leadership.md#lead-disruptive-star) | Гипотетическая проблема взаимодействия; тип applied scenario, наблюдаемое поведение и справедливый процесс | Тот же отчёт перечитан; гипотетическая суть совпадает |
| [lead-reorganisation-retention](../themes/engineering-leadership.md#lead-reorganisation-retention) | Реальное сложное изменение с уходами; тип behavioural, правдивый опыт и последствия для оставшейся команды | Тот же отчёт перечитан; суть состоявшихся уходов совпадает |
| [lead-strategic-hiring](../themes/engineering-leadership.md#lead-strategic-hiring) | Последний стратегический найм инженера; поведенческий ответ различает личные полномочия, планку и результаты | Гайд Stripe перечитан; последний стратегический найм и планка теперь согласованы; источник остаётся вторичным |

Для каждого исправления согласованы EN/RU описания проверяемого навыка, чек-листы и ответы. Уточнения редакционные, не стенограмма. Google остаётся отчётом участника об общем EM-интервью; Stripe — общим подготовительным гайдом менеджмента. Исходные URL перенаправили на тот же материал Aced. Относительное время обновления не устанавливает дату публикации или интервью. [Meta EM][META-EM] снова пытались открыть 05.10.2026; страница осталась недоступна: `prog-cross-team-delivery` **не проверен заново**, у источника сохранена дата последнего успешного чтения.

### Добавленное покрытие и семантические проверки

| Вопрос и приоритет | Роль/полномочия и отдельное решение | Учебное покрытие теперь | Свидетельство интервью |
| --- | --- | --- | --- |
| [ops-ai-portfolio-allocation](../themes/ai-operating-model.md#ops-ai-portfolio-allocation), L71 | Head/Director с полномочиями портфеля; распределить деньги и людей после сокращения между зависимыми инициативами | Прямой ограниченный вопрос, ответ EN/RU, чек-лист и чтение по оценке вариантов; глубже предшественников о roadmap | Сгенерирован по допустимой теме операционной модели радара; без работодателя |
| [ops-ai-build-buy-exit](../themes/ai-operating-model.md#ops-ai-build-buy-exit), L72 | Владелец инвестиций; утвердить продление или замену с договорными сроками и проверенным профинансированным выходом | Прямой вопрос о возможностях организации и непрерывности, шире выбора модели | Сгенерирован; облачное руководство поддерживает только обучение |
| [lead-managers-accountability](../themes/engineering-leadership.md#lead-managers-accountability), L73 | Руководитель менеджеров; согласовать границы и обещания руководству, сохраняя полномочия менеджеров | Прямой вопрос, ответ и проверки прав решений, шире одной платформенной команды | Сгенерирован; роль/процесс GitLab не являются свидетельством вопроса |
| [prod-ai-stop-investment](../themes/ai-product-strategy.md#prod-ai-stop-investment), L74 | Владелец продуктовых инвестиций; остановить или сузить работающий продукт и поддержать пользователей | Вопрос объединяет дополнительную пользу, неизвестность и закрытие, шире первоначального запуска | Сгенерирован; чтение о метриках/экспериментах не подтверждает интервью |
| [prog-incident-without-rollback](../themes/program-delivery.md#prog-incident-without-rollback), L75 | TPM/координация программы; сдержать ущерб и обосновать повторный запуск без отката | Прямой вопрос о полномочиях инцидента, клиентах и восстановлении | Сгенерирован; не опубликованный вопрос AI TPM |
| [lead-ai-interview-redesign](../themes/engineering-leadership.md#lead-ai-interview-redesign), L76 | EM/владелец найма; выбрать объявленные правила инструментов и оценить индивидуальное суждение | Существующий вопрос получает ответ EN/RU и уточнённый чек-лист без универсального правила AI | Сгенерированное происхождение сохранено; официальные блоги — чтение |

У всех шести есть чек-лист из трёх пунктов, первичное чтение и ответы по 100–180 слов на каждом языке. Порядок 1–70 сохранён. Пять новых вопросов используют допустимые темы Leadership-радара и явно задают полномочия в сценарии, не выдумывая уровни работодателей. Смысловое сравнение проверило новое измерение решения относительно roadmap, платформенной команды, выбора модели, запуска и готовности. Одного сравнения похожих слов для этого недостаточно.

Тридцать пробелов чтения в семи темах автора Leadership закрыты подходящими первичными материалами; параллельный проход Engineering закрыл остальные. Пригодность проверялась по каждому вопросу: например, офлайн-синхронизация для полевого каталога, сопоставление спроса и предложения для cold start, обсуждение FINRA для декомпозиции финансовых расследований и компоненты вознаграждения для вопроса о миссии без роста акций. Источники описывают методы или предметную область, не новые случаи интервью. Исследовательская неопределённость и межкомандная готовность уже имеют прямые вопросы; руководство ведёт к их ответам, не дублируя их.

### Более сильные источники процесса и их пределы

Все три страницы открыты 05.10.2026. [Подготовка TPM в Amazon](https://amazon.jobs/content/en/how-we-hire/tpm-interview-prep) не имеет установленной даты публикации и описывает общий телефонный скрининг TPM, письменное задание и цикл из пяти интервью, включая системный дизайн. Страница Amazon теперь отделяет эти официальные этапы от существующего вторичного пути AI-PM.

[Страница Engineering Director GitLab](https://handbook.gitlab.com/job-description-library/engineering/development/management/director/) содержит настоящий раздел процесса найма и дату изменения 12.03.2026. [Product Management Leadership](https://handbook.gitlab.com/job-description-library/product/product-management-leadership/) также описывает этапы найма Director; дата публикации здесь не установлена. Они подтверждают ограниченные общие утверждения об обязанностях и процессе Director. Они не дают новых AI-кейсов, независимого подтверждения другим издателем или доказательства одинаковых полномочий всех Director. Страница компании GitLab не добавлялась только по этим документам одного издателя.

Прямые свидетельства от первого лица о вопросах Head/Director и специализированного AI TPM остаются пробелом. Исправления источников, учебные добавления и официальные процессы улучшают разные стороны материала; ни одно не означает свежую проверку всего банка. Руководство по вопросам сохраняет изменённые условия и общую шкалу устного ответа без обязательных кодовых упражнений, лабораторных работ, проектов или автоматического оценщика.

## Неоднозначные назначения и оставшиеся пробелы

Теги ролей редакционные. В Leadership входят вопросы FDE, инженеров оценки, инференса и исследований. `sd-model-api`, `agt-erp-writes`, `inf-runtime-choice`, `llm-compute-optimal`, `code-refactoring` — техническое ревью или дополнительная глубина; они не заменяют найм, развитие людей и распределение ресурсов. `lead-engineering-persuasion` проверяет продуктовое партнёрство, не управление людьми. `prod-handyman-marketplace` и `prod-volunteer-cold-start` остаются общими PM-упражнениями, хотя рассказ относится к AI-PM треку.

Платежи, клинические записи, актуальность права, проверка возраста и робототехника нужны по ответственности конкретной роли. Короткие чек-листы и общие ссылки не устанавливают юридическую, медицинскую или физическую безопасность решения. Дополнение не делает их универсальным P0. Неуказанный уровень остаётся неуказанным; учебный тег `senior` не подтверждает уровень работодателя. Бюджетные права, прямые подчинённые, менеджеры в подчинении и принятые решения указываются отдельно.

Приоритет источников — прямые публичные свидетельства об интервью Head/Director и AI TPM от дополнительных независимых издателей. Приоритет обучения — собственные результаты: решения, расчёты, критерии запуска и повторные попытки. Выполненный кейс добавляет учебный результат, а не опубликованный вопрос интервью или профессиональное достижение.

## Исследование ролей и границы источников

Следующие официальные страницы открыты **05.10.2026**. Дата означает публикацию, если установлена; иначе страница текущая, без даты. Это отдельные примеры работодателей, не репрезентативное исследование рынка.

| Источник | Дата | Что именно использовано; ограничение |
| --- | --- | --- |
| [Anthropic PM, Claude Science](https://job-boards.greenhouse.io/anthropic/jobs/5394887008) | Текущая, без даты | Вакансия связывает исследование потребностей учёных, roadmap и оценку; интервью не описывает |
| [Anthropic EM, Data Infrastructure](https://job-boards.greenhouse.io/anthropic/jobs/5426135008) | Текущая, без даты | Развитие людей, надёжность/стоимость платформы и найм; работа в AI-компании не доказывает AI-специализацию интервью |
| [Anthropic TPM, Research](https://job-boards.greenhouse.io/anthropic/jobs/5203545008) | Текущая, без даты | Координация исследований/разработки, меняющиеся приоритеты и эксплуатация; вопросов интервью нет |
| [Pfizer AI Oncology Portfolio Lead, Director](https://www.pfizer.com/about/careers/job/4964531?langcode=en) | Текущая, без даты | Явно роль индивидуального специалиста: Director не доказывает управление людьми или бюджетом |
| [Anthropic, AI-resistant technical evaluations](https://www.anthropic.com/engineering/AI-resistant-technical-evaluations) | 21.01.2026 | Пример изменения задания для performance-инженеров; повод калибровать практику, не универсальное разрешение AI на интервью |
| [Monzo PM][MONZO-PM] / [Senior Staff+][MONZO-STAFF] | 04.10.2022 / 02.05.2025 | Официальные базовые процессы общего PM и старшего IC соответственно |
| [Интервьюер на Хабре][HABR] | Дата не установлена в этой проверке | Личный подход автора к enterprise AI PM-интервью, не процесс всей компании |
| Рассказы и руководства из таблицы двадцати проверок | Без даты/динамические | Относительный timestamp не устанавливает точную дату интервью; руководства вторичны, рассказы индивидуальны |

Дополнительная вакансия Director в Sony Pictures появилась в поиске, но при открытии не было читаемого текста; требования director-ролей по ней не устанавливались. Вакансия Anthropic Business Technology PM перенаправляла на список вакансий и исключена. Недоступные страницы и поисковые сниппеты не засчитаны как успешная проверка.

[HABR]: https://habr.com/ru/articles/1038482/
[META-PM]: https://www.tryexponent.com/experiences/meta-facebook-product-manager-interview-618bfd
[GOOGLE-EM]: https://www.tryexponent.com/experiences/google-staff-engineering-manager-interview-fd33b1
[ANTHROPIC-EM]: https://www.tryexponent.com/experiences/anthropic-engineering-manager-interview-170078
[META-EM]: https://www.tryexponent.com/experiences/meta-facebook-engineering-manager-interview-916dc8
[MONZO-PM]: https://monzo.com/blog/2022/10/04/product-management-at-monzo-the-interview-process
[MONZO-STAFF]: https://monzo.com/blog/demystifying-the-senior-staff-engineering-interview-process
[STRIPE]: https://www.tryexponent.com/blog/stripe-interview-process
[OPENAI-PM]: https://www.tryexponent.com/guides/openai-product-manager-interview
[AMAZON-PM]: https://www.tryexponent.com/guides/amazon-ai-product-manager-interview
