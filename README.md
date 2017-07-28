alfastrah-kasko-calc
====================

Калькулятор КАСКО Альфа страхование

### Настройка локальной машины для запуска скрипта
 
1. Установить Firefox
2. Установить Python (https://www.python.org/downloads/release/python-342/)
3. Прописать в переменную окружения PATH к установленному каталогу с python.exe (по умолчанию это C:\Python34\) и добавить путь к C:\Python34\Scripts
4. Установить git-клиента https://git-scm.com/downloads
5. Запустить консоль git
6. Клонировать репозиторий себе на локальную машину
```bash
git clone https://github.com/efpato/alfastrah.git
```
7. Перейти в склонированный каталог и выполнить:
```bash
cd alfastrah
pip install -r requirements.txt
```

УСПЕХ! Вы готовы к использованию скрипта локально на своей виндовой машине

### Использование

```bash
python kasko-calc sample.xlsx
```
На выходе получаем Excel-файл sample.out.xlsx
