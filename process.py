from pathlib import Path
import csv
try:from bs4 import BeautifulSoup
except ImportError:raise SystemExit('Install dependencies: pip install beautifulsoup4')
BASE=Path(__file__).parent;OUT=BASE/'output';OUT.mkdir(exist_ok=True)
soup=BeautifulSoup((BASE/'input/fictional_shop.html').read_text(encoding='utf-8'),'html.parser')
records=[]
for item in soup.select('article.product'):
    records.append([item.get('data-sku',''),item.select_one('.title').get_text(strip=True),item.select_one('.price').get_text(strip=True).replace('$',''),item.select_one('.category').get_text(strip=True)])
with (OUT/'scraped_products.csv').open('w',newline='',encoding='utf-8') as f:w=csv.writer(f);w.writerow(['sku','product','price_usd','category']);w.writerows(records)
print(f'Extracted {len(records)} products from local HTML sample')
