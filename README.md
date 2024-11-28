## Климатический анализ c использованием Streamlit для визуализации данных


### How to tun?
- install requirements
```bash
pip install -r requirements.txt --no-cache-dir
```
- скачайте датасет (https://www.google.com/url?q=https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data?resource%3Ddownload&sa=D&source=docs&ust=1732716655094480&usg=AOvVaw0oSFKHht6h_sRWnQeSgOtV) 
- unzip file и поместите в папку `data` по пути:
```bash
data/GlobalLandTemperaturesByCity.csv.zip
```
- run streamlit application
```bash
streamlit run main.py     
```

### How to add new section (page)? 
- create new `page.py` file in the sections folder
- add new section in the `main.py`

---- 

## Страницы

### 1. Общий анализ

![img.png](img/img.png)

### 2. Анализ трендов температуры

![img_1.png](img/img_1.png)

![img_2.png](img/img_2.png)

- при вводе неверного города

![img_5.png](img/img_5.png)

### 3. Проверка гипотезы на глобальное потепление

![img_3.png](img/img_3.png)


### 4. Карта метеостанций

![img_4.png](img/img_4.png)

### 5. По странам

![img.png](img/img_7.png)
