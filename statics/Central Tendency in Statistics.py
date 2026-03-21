# # # #         Mean
# # # # q 1 Arithmetic Mean

# # # data = [10, 20, 30, 40, 50]
# # # am=sum(data)/len(data)
# # # print(int(am))

# # # Q 2 --> Python function banao jo list ka mean return kare.
# # # def mean(list):
# # #     # for i in range(len(list)):
# # #     return sum(list)/len(list)
# # # list=[10, 20, 30, 40, 50]
# # # mean(list)

# # # Q 3 --> Weighted Mean
# # values = [60, 70, 80]
# # weights = [1, 2, 3]
# # weighted_sum=0
# # total_weight=0
# # for i in range(len(values)):
# #     weighted_sum+= values[i]*weights[i]
# #     total_weight+=weights[i]
# # weighted_mean=weighted_sum/total_weight
# # print(weighted_mean)



# # Q 3 --> Geometric Mean
# # data = [2, 4, 8]

# # p=1
# # for x in data:
# #     p*=x
# # print(p ** (1/len(data)))

# #  Q 4 -> Harmonic Mean
# # data = [60, 40]

# # s=0
# # for x in data:
# #     s+=1/x
# # hm=len(data)/s
# # print(hm)




#                 # 2 --->  meadian
# # odd number
# # data = [7, 3, 9, 5, 1]
# # def meadian(data):
# #     data.sort()
# #     n=len(data)
# #     if n%2!=0:
# #         return data [n//2]
# #     else:
# #         return ((data[n//2-1])+(data[n//2]))/2
# # print(meadian([12, 5, 8, 10]))
# # print(meadian(data))



# #           3 mode
# # from collections import Counter
# # def mode(data):
# #     freq=Counter(data)
# #     max_freq=max(freq.values())
# #     node=[k for k,v in freq.items() if v==max_freq]
# #     if len(node)==len(freq):
# #         return "no mode"
# #     return node
# # print(mode([1,2,2,3,4]))      # [2]
# # print(mode([1,1,2,2,3]))      # [1, 2]
# # print(mode([1,2,3,4]))        # No Mode


















# # mode practice
# from collections import Counter
# def mode(data):
#     freq=Counter(data)
#     max_freq=max(freq.values())
#     node=[k for k , v in freq.items() if v==max_freq]
#     if len(node)==len(freq):
#         print("no node")
#     return node
# data=[2,3,2,4,2,1,3,2,1]
# print(mode(data))










#  5  --> Find the Second Quartile for the data 10, 30, 5, 12, 20, 40, 25, 15, 18.
# def quartile(data):
#     data.sort()
#     n=len(data)
#     q1=(n+1)//2
#     return data[q1]
# data=[10, 30, 5, 12, 20, 40, 25, 15, 18]
# print(quartile(data))
