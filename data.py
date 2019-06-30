import logs
import json


logger = logs.main_logger

# Indexing callback data
cbMain = 'back_to_main_menu'
cbSubj = 'subjects'
cbSch = 'schedule'
cbSch_del1 = 'sched_del_start'
cbSch_del2 = 'sched_del_item_'
cbSch_del3 = 'sched_del_all'
cbSch_add1 = 'sched_add'
cbSch_add2 = 'sched_add_item_'
cbSch_edi1 = 'sched_edit'
cbSch_edi2 = 'sched_edit_subj_'
cbSch_edi3 = 'sched_edit_item_'
cbSubj_del1 = 'subj_del_start'
cbSubj_del2 = 'subj_del_item_'
cbSubj_del3 = 'subj_del_all'
cbSubj_add1 = 'add_subject'
cbSubj_edi1 = 'edit_subject_start'
cbSubj_edi2 = 'edit_subject_item'

# Reading JSON data
def get_data(id):
    id = str(id)
    lst = [
        'Physical Education',
        'Computer architecture',
        'System Programming',
        'Computer networks',
        'Peripherals',
        'Mechanical drawing',
        'Computer circuitry'
    ]
    lst = sorted(lst)
    sch = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
    default = {'items': lst, 'sched': sch}  # Setting a default library

    logger.info('= = = = = Requesting user info... = = = = =')

    with open("db.json", "r", encoding='utf-8') as read_file:  # Reading dictionary from database (JSON file)
        user_info = json.load(read_file)

    logger.info(f'Input user id: {id}')
    logger.info(f'Result (if not found or empty you will see default settings):\n{user_info.get(id, default)}')

    if user_info.get(id, 0) == 0:  # Looking for our user's ID in the dictionary
        user_info.update({id: default})  # If ID is not found, then creating a new entry
        with open("db.json", "w", encoding='utf-8') as write_file:  # Rewriting new data in case of new entry
            json.dump(user_info, write_file, ensure_ascii=False)
        logger.info('Created new entry')

    logger.info('= = = = = Request completed = = = = =')
    return user_info[id]


# Updating JSON data
def set_data(id, data):
    id = str(id)
    logger.info('= = = = = Saving user info... = = = = =')
    logger.info(f'Input user id: {id}')
    with open("db.json", "r", encoding='utf-8') as read_file:  # Reading dictionary from database (JSON file)
        user_info = json.load(read_file)
    user_info.update({id: data})
    with open("db.json", "w", encoding='utf-8') as write_file:
        json.dump(user_info, write_file, ensure_ascii=False)
    logger.info('= = = = = Save completed = = = = =')


# Clearing schedule
def sched_clear(sched, items):
    logger.info(f'sched_clear(): Started. Input: {sched}, {items}')
    empty = True
    for j in sched:
        if -1 < int(j) < len(items):
            empty = False
    if empty:
        sched = []
    logger.info(f'sched_clear(): Finished. Result: {sched}')
    return sched
