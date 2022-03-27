# from icrawler.builtin import GoogleImageCrawler
import os
from datetime import date,timedelta
from icrawler.builtin import GoogleImageCrawler


# # GoogleImageCrawler 객체 생성
# google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
# google_crawler.crawl(keyword='펭수', max_num=1000)

# 이미지 저장 폴더 경로
save_dir1 = os.path.join('..', '..', 'images1')


google_crawler = GoogleImageCrawler(
    parser_threads=2, 
    downloader_threads=4,
    storage={'root_dir': save_dir1})



kwd = '리트리버'    
for years in range(2015,2021):
    google_crawler.crawl(
        keyword='\"'+kwd+' after : '+str(years)+'-01-01 before : '+str(years)+'-03-31\"',
        max_num=1000,
        max_size =(224,224),
        file_idx_offset='auto'
        # date_min=None,
        # date_max=Nonea
     )
    google_crawler.crawl(
        keyword='\"'+kwd+' after : '+str(years)+'-04-01 before : '+str(years)+'-6-31\"',
        max_num=1000,
        max_size =(224,224),
        file_idx_offset='auto'
        # date_min=None,
        # date_max=Nonea
     )
    google_crawler.crawl(
        keyword='\"'+kwd+' after : '+str(years)+'-06-01 before : '+str(years)+'-9-31\"',
        max_num=1000,
        max_size =(224,224),
        file_idx_offset='auto'
        # date_min=None,
        # date_max=Nonea
     )
    google_crawler.crawl(
        keyword='\"'+kwd+' after : '+str(years)+'-09-01 before : '+str(years)+'-12-31\"',
        max_num=1000,
        max_size =(224,224),
        file_idx_offset='auto'
        # date_min=None,
        # date_max=Nonea
     )





# google_crawler1 = GoogleImageCrawler(
#     parser_threads=2, 
#     downloader_threads=4,
#     storage={'root_dir': save_dir1})
# google_crawler2 = GoogleImageCrawler(
#     parser_threads=2, 
#     downloader_threads=4,
#     storage={'root_dir': save_dir1})
# google_crawler3 = GoogleImageCrawler(
#     parser_threads=2, 
#     downloader_threads=4,
#     storage={'root_dir': save_dir1})



# google_crawler1.crawl(
#     keyword='\"골든리트리버 after : 2019-01-01 before : 2019-12-31\"',
#     max_num=1000,
#      file_idx_offset='auto'
#     # date_min=None,
#     # date_max=Nonea
#     )
# google_crawler2.crawl(
#     keyword='\"골든리트리버 after : 2020-01-01 before : 2020-12-31\"',
#     max_num=1000,
#      file_idx_offset='auto'
#     # date_min=None,
#     # date_max=Nonea
#     )
# google_crawler3.crawl(
#     keyword='\"골든리트리버 after : 2021-01-01 before : 2021-12-31\"',
#     max_num=1000,
#      file_idx_offset='auto'
#     # date_min=None,
#     # date_max=Nonea
#     )
