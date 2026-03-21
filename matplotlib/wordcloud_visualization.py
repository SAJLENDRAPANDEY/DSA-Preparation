from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
# text = """
# Python is easy to learn.
# Python is powerful.
# Python is used for Data Science, AI, and Web Development.
# """
# wordcloud=WordCloud(
#     height=400,
#     width=600,
#     background_color='white'
# ).generate(text)
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()



# 1 --> generates word clod from list words
# list=['apple','apple','banana','guavava','apple']
# text=" ".join(list)
# word=WordCloud(height=400,width=600,background_color='lightblue').generate(text)
# plt.imshow(word)
# plt.axis('off')
# plt.show()


# 2-->Word Cloud from Pandas DataFram
# data=pd.DataFrame({
#     'name':['yash','yash','yash','raj','ram']
# })
# word=" ".join(data['name'])
# wordcloud=WordCloud(colormap='viridis').generate(word)
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()


#  3 --> 