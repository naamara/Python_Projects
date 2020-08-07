def main():
    """ Note1: this code or program is written for the hacker news website, a website that updates you about the latest tech, software stuffs,so
    instead of manually going to the site to check for the latest topics/ headlines with highest points, this code does 
    that automatically for you irrespective of the page you enter and saves the extracted links you want in excel as a csv file.
    
    Note2: the word 'title', 'headlines', 'topics' will be used interchangeably in the comments
    """
    
    
    import requests, bs4
        # the request library is used to connect to the internet while beautifulsoup library is used to pull out data out of hmtl
    
    import pandas as pd
        # this library is used to convert the extracted data to a dataframe
    maximum_page=21
        # the maximum page for the hacker news website is 21
    
    page_num=int(input('for headlines on any page of the hacker news, enter page number from 1-21: '))
        # an interactive interface that allows you to enter the page number you want
    while page_num <= maximum_page:
        page_url='https://news.ycombinator.com/news?p=' +str(page_num)
        break
    res =requests.get(page_url)
        #this code requests for the information in the url from the server and stores the result in a python object
    
    soup_obj=bs4.BeautifulSoup(res.text,'html.parser')
        # a beautifulsoup object is created which takes the html content and parses the html
    
    links=soup_obj.select('.storylink')
        # a css selector is used to get all the links on that page that belongs to a class of "story link"
    
    sub_text=soup_obj.select('.subtext')
        # a css selector is used to get all the links on that belongs to a  class of "substext"
        

    def to_get_links(func,link,subtext):
        """ note: this fuction takes 3 positional argument,a fuction,the links and subtext as arguments"""
    
        list=[] # an empty list 
        for index,text in enumerate(link): 
            # this iterates through the links or topics in the page
        
            headline=text.get_text() 
                # this codes extracts only the text from each headline or topics
            lnk=text.get('href',None) 
                # this code is used to extract the links to those headlines
            
            points=subtext[index].select('.score')
                # for each headline is given a point or vote, the code extracts all the points with a class "score"
            
            if len(points) !=0: # in cases where topics/headlines do not have points, this code considers  headline or topics with points/votes
                scores=int(points[0].get_text().strip().replace('points','')) 
                    # after getting the subtext, we are only interested in the points in the subtext, this code cleans it and return an integer
                
                if scores > 79:
                    # only points/votes of 80 and above are extracted
                    list.append({'headline':headline, 'links':lnk,'score':scores}) # a dictionary of the headline,links and scores/points are added to the empty list
        return func(list) 
            # a function is returned    
                        
    
    def sorting_method(li_dict):
        """ this function accepts the list and sorts/arranges the list of dictionary by points in descending order using lambda"""
        sorted_list_of_dict= sorted(li_dict, key=lambda x:x['score'],reverse=True)
        
        df=pd.DataFrame(sorted_list_of_dict)
            # the sorted list of dictionary is converted to a dataframe using the pandas dataframe
        
        return df.to_csv('scraped web page.csv')
            # the dataframe is exported as a csv file and saved as "scraped web page" which can be opened with excel or a text editor
    
    to_get_links(sorting_method,links,sub_text)

if __name__=='__main__':
    main()
