def solution(todo_list, finished):
    unfinished_tasks = [task for task, is_done in zip(todo_list, finished) if not is_done]
    return unfinished_tasks