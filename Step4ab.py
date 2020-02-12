import csv
import sys
import fileinput

class Counter():
    
    def __init__(self):
        self.line_handlers = dict(
            A=self.handle_view_count_line,
            B=self.handle_qnr
        )

    def count(self):
        self.view_count = 0

        self.prev_article = (None, None)

        for line in fileinput.input():
            lang, title, linetype, q_views = line.split(' ')
            line_handler = self.line_handlers[linetype]
            line_handler(lang, title, linetype, q_views)

    def handle_view_count_line(self, lang, title, linetype, views):
        title = title.lower()  
        if (lang, title) == self.prev_article:
            self.view_count += views
        else:
            self.view_count = views
        self.prev_article = (lang, title)
        
    def handle_qnr(self, lang, title, linetype, qnr):
        if (lang, title) == self.prev_article:
            #qviews = qnr[:-1] , self.view_count
            print( qnr[:-1] , self.view_count)