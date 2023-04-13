# wash dishes > cook dinner
# cook dinner > clean windows
# clean windows > wash dishes

def task_decider(first_task, second_task):
    if first_task.description == "wash dishes" and second_task.description == "cook dinner":
        return first_task.description
    
    if first_task.description == "cook dinner" and second_task.description == "clean windows":
        return first_task.description
    
    if first_task.description == "clean windows" and second_task.description == "wash dishes":
        return first_task.description
    


    # else: 
    #     return "help"



    # if first_task and second_task:
    #     task_to_do = first_task
    # if second_task and third_task:
    #     task_to_do = second_task
    # if third_task and first_task:
    #     task_to_do = third_task