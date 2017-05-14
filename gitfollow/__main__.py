from .gitfollow import *

if __name__=="__main__":
    time_1=time.perf_counter()
    username=input("Please Enter Your Github Username : ")
    print("Collecting Follower Information ...")
    list_1=follower_list_gen(username)
    file = open(username + "_follower.log", "w")
    file.write("\n".join(list_1))
    file.close()
    print('Collecting Following Informnation ...')
    list_2=following_list_gen(username)
    file = open(username + "_following.log", "w")
    file.write("\n".join(list_2))
    file.close()
    following_not_follower=[]
    file=open(username+"_dif.log","w")
    for i in list_2:
        if i not in list_1:
            following_not_follower.append(i)
            file.write(i+"\n")
    file.close()
    time_2=time.perf_counter()
    print("Data Generated In "+str(time_2-time_1)+" sec")
    gc.collect()











