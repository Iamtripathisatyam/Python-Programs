######################### Time Analysis in Calculationg length ##############################################

from operator import length_hint
import time

a=[]
n=int(input("Enter the Number of Elements: "))
for i in range(0,n):
    element=int(input())
    a.append(element)

################ Using for Loop ###################

start_for_time=time.time()
count=0
for i in a:
    count+=1
end_for_time=str(time.time()-start_for_time)


################# Using len function ###################

start_len_time=time.time()
list_len=len(a)
end_len_time=str(time.time()-start_len_time)



################## Using length_hint function #########################

star_len_hint=time.time()
list_lens=length_hint(a)
end_len_hint=str(time.time()-star_len_hint)


print(f"Using for Loop: {count}, Using len(): {list_len}, Using length_hint(): {list_lens}")
print(f"for Time: {end_for_time}, len Time: {end_len_time}, length_hint Time: {end_len_hint}")
