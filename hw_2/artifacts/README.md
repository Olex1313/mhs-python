# Задание 2.1

Решение в `2.1.py`

Артефакт - `hw_2/artifacts/example_2.1.tex`

## Запуск

```bash
python3 2.1.py --output <filename>
```

# Задание 2.2
Решение в `2.2.py`

Артефакты - `hw_2/artifacts/output/*`

[Pypy](https://pypi.org/project/latex-generator-olex1313/1.0.0/)

## Запуск

```bash
python3 .\2.2.py <path_to_image> --output <filename>
```

Сборка:
```bash
python3 setup.py sdist && twine upload dist/*
```

# Задание 2.3

Артефакты - `hw_2/artifacts/Dockerfile` и `hw_2/artifacts/docker-compose.yaml`

Для запуска в консоли нужно:
```bash
cd hw_2 #перейти в директорию hw_2
docker compose up
```

После, сгенерированные pdf и tex файлы будут в папке `hw_2/output`