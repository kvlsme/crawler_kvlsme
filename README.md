# crawler_kvlsme

Template for crawler based on scrapy-crawler

## Installation

1. Install Scrapy:
    ```bash
    pip3 install scrapy
    ```

2. Start a new Scrapy project:
    ```bash
    scrapy startproject name_of_your_project
    ```

3. Run the crawler:
    ```bash
    scrapy crawl template
    ```

## Usage

1. Modify the `start_urls` in `template.py` to include the URLs of the categories you want to scrape.
2. Adjust the XPath expressions in the `parse` and `parse_product` methods to match the structure of the target website.
3. Run the crawler using the command:
    ```bash
    scrapy crawl template
    ```

## Dependencies

- Python 3.x
- Scrapy

## Special Notes

- Ensure that the XPath expressions in the `template.py` file are updated to match the structure of the website you are scraping.
- The output is saved in a CSV file named `template.csv`. You can change this name in the `__init__` method of the `Template` class.

## Code Structure

- `template.py`: Contains the Scrapy spider code. It defines the crawler's name, start URLs, and parsing logic.
    - `start_urls`: List of URLs to start crawling from.
    - `parse`: Method to parse the category pages and extract product links.
    - `parse_product`: Method to parse individual product pages and extract required fields.
    - `get_next_page_url`: Method to generate the URL for the next page.

## Contributors

- Placeholder for contributors

## License

This project is licensed under the terms of the Mozilla Public License Version 2.0. See the [LICENSE](LICENSE) file for details.

---

# crawler_kvlsme

Шаблон для краулера на основе scrapy-crawler

## Установка

1. Установите Scrapy:
    ```bash
    pip3 install scrapy
    ```

2. Создайте новый проект Scrapy:
    ```bash
    scrapy startproject name_of_your_project
    ```

3. Запустите краулер:
    ```bash
    scrapy crawl template
    ```

## Использование

1. Измените `start_urls` в `template.py`, чтобы включить URL категорий, которые вы хотите сканировать.
2. Настройте выражения XPath в методах `parse` и `parse_product`, чтобы они соответствовали структуре целевого сайта.
3. Запустите краулер с помощью команды:
    ```bash
    scrapy crawl template
    ```

## Зависимости

- Python 3.x
- Scrapy

## Особые примечания

- Убедитесь, что выражения XPath в файле `template.py` обновлены в соответствии со структурой сайта, который вы сканируете.
- Вывод сохраняется в CSV файл под названием `template.csv`. Вы можете изменить это имя в методе `__init__` класса `Template`.

## Структура кода

- `template.py`: Содержит код паука Scrapy. Определяет имя краулера, начальные URL и логику парсинга.
    - `start_urls`: Список URL для начала сканирования.
    - `parse`: Метод для парсинга страниц категорий и извлечения ссылок на продукты.
    - `parse_product`: Метод для парсинга отдельных страниц продуктов и извлечения необходимых полей.
    - `get_next_page_url`: Метод для генерации URL для следующей страницы.

## Контрибьюторы

- Заполнитель для контрибьюторов

## Лицензия

Этот проект лицензирован на условиях Mozilla Public License Version 2.0. См. файл [LICENSE](LICENSE) для получения деталей.
