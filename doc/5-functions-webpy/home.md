## Импортировать базу компаний.

Сайт flagma.kz



    from django.core.management.base import BaseCommand, CommandError

    from app.models import Person, MainDocuments, Person2Document, Company, City, Person2Company, Import
    import re
    import psycopg2
    import bs4
    import requests
    import time

        def parse_company(c):
            try:
                city = City.objects.get(name_ru__icontains=c.city_text)
                c.city = city
                c.save()
            except:
                print('City not found')

            namear = c.faunders_text.split(',')
            p = Person()
            p.raw_name = namear[0]
            p.role = namear[1]
            p.source = 'flagma.kz'
            p.save()
            p.parse()

            p2c = Person2Company()
            p2c.company = c
            p2c.person = p
            p2c.save()

            print('Saving person %s' % namear[0])
            


        class Command(BaseCommand):

            def handle(self, *args, **options):
                print('Importing.')   
                Company.objects.all().delete()
                Person.objects.filter(source='flagma.kz').delete()
                Person2Company.objects.all().delete()
                urls = []
                for cnt in range(1,1000):
                    urls.append('https://flagma.kz/kompanii-k-%s.html' % cnt)
                
                for url in urls:
                    print("Importing %s" % url)
                    time.sleep(1)
                    i = Import()
                    i.url = url
                    i.save()
                    rez = requests.get(url)
                    soup = bs4.BeautifulSoup(rez.text, 'html.parser')
                    items = soup.findAll('div',{"class": "page-list-item-info"})
                    for i in items:
                        name = i.find('a').text
                        location = i.find('span',{"itemprop": "location"}).text
                        boss = i.find('span',{"itemprop": "employee"}).text
                        arrboss = boss.split(',')
                        c = Company()
                        c.name_ru = name
                        c.name_kz = name
                        c.faunders_text = boss
                        c.city_text = location
                        c.save()
                        parse_company(c)
                        print('Saving.....%s' % name)
                    
                    
                    
