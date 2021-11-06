# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CsdnHotWordsPipeline:

    def __init__(self):
        self.file = open('result.txt', 'w', encoding='utf-8')
        self.all_words = []

    def process_item(self, item, spider):
        self.all_words.append(item)
        return item

    def close_spider(self, spider):
        key_word_dic = {}
        for y in self.all_words:
            print(y)
            for k, v in y['words'].items():
                if k.lower() in key_word_dic:
                    key_word_dic[k.lower()] += v
                else:
                    key_word_dic[k.lower()] = v
        word_count_sort = sorted(key_word_dic.items(),
                                 key=lambda x: x[1], reverse=True)
        for word in word_count_sort:
            self.file.write('{},{}\n'.format(word[0], word[1]))
        self.file.close()
