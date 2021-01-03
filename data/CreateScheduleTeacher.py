import pymongo



def ScheduleTeacher_db_init():
    client = pymongo.MongoClient()
    mydb = client['EZSchooldb']

    mycol = mydb['ScheduleTeacher']

    data = [
        {
            'id': '312208523',
            "monday1": ["הסטוריה כיתה ב", "הסטוריה כיתה ב", "תנך כיתה א", "חשבון כיתה א", "חשבון כיתה א"],
            "sunday1": ["", "", "", "", ""],
            "tuesday1": ["תנך", "תנך", "תנך", "עברית", "עברית"],
            "wednesday1": ["עברית", "עברית", "חשבון", "חשבון", "חשבון"],
            "thursday1": ["חשבון", "חשבון", "", "חשבון", "הסטוריה"]},
        {
            'id': '312208524',
            "monday2": ["הסטוריה", "הסטוריה", "תנך", "חשבון", "חשבון"],
            "sunday2": ["", "הסטוריה", "חשבון", "חשבון", "חשבון"],
            "tuesday2": ["תנך", "תנך", "תנך", "עברית", "עברית"],
            "wednesday2": ["עברית", "עברית", "חשבון", "חשבון", "חשבון"],
            "thursday2": ["חשבון", "חשבון", "", "חשבון", "הסטוריה"]},
        {
            'id': '312208525',
            "monday3": ["הסטוריה כיתה ב", "הסטוריה כיתה ב", "תנך כיתה א", "חשבון כיתה א", "חשבון כיתה א"],
            "sunday3": ["", "", "", "", ""],
            "tuesday3": ["תנך", "תנך", "תנך", "עברית", "עברית"],
            "wednesday3": ["עברית", "עברית", "חשבון", "חשבון", "חשבון"],
            "thursday3": ["חשבון", "חשבון", "", "חשבון", "הסטוריה"]},
        {
            'id': '312208526',
            "monday4": ["הסטוריה כיתה ב", "הסטוריה כיתה ב", "תנך כיתה א", "חשבון כיתה א", "חשבון כיתה א"],
            "sunday4": ["", "", "", "", "הסטוריה כיתה א"],
            "tuesday4": ["תנך", "תנך", "תנך", "עברית", "עברית"],
            "wednesday4": ["עברית", "עברית", "חשבון", "חשבון", "חשבון"],
            "thursday4": ["חשבון", "חשבון", "", "חשבון", "הסטוריה"]},
        {
            'id': '312208527',
            "monday5": ["הסטוריה כיתה ב", "הסטוריה כיתה ב", "תנך כיתה א", "חשבון כיתה א", "חשבון כיתה א"],
            "sunday5": ["", "", "", "", ""],
            "tuesday5": ["תנך", "תנך", "תנך", "עברית", "עברית"],
            "wednesday5": ["עברית", "עברית", "חשבון", "חשבון", "חשבון"],
            "thursday5": ["חשבון", "חשבון", "", "חשבון", "הסטוריה"]},
        {
            'id': '312208528',
            "monday6": ["הסטוריה כיתה ב", "הסטוריה כיתה ב", "תנך כיתה א", "חשבון כיתה א", "חשבון כיתה א"],
            "sunday6": ["", "", "", "", ""],
            "tuesday6": ["תנך", "תנך", "תנך", "עברית", "עברית"],
            "wednesday6": ["עברית", "עברית", "חשבון", "חשבון", "חשבון"],
            "thursday6": ["חשבון", "חשבון", "", "חשבון", "הסטוריה"]},
        {
            'id': '312208529',
            "monday7": ["הסטוריה כיתה ב", "הסטוריה כיתה ב", "תנך כיתה א", "חשבון כיתה א", "חשבון כיתה א"],
            "sunday7": ["", "", "", "", ""],
            "tuesday7": ["תנך", "תנך", "תנך", "עברית", "עברית"],
            "wednesday7": ["עברית", "עברית", "חשבון", "חשבון", "חשבון"],
            "thursday7": ["חשבון", "חשבון", "", "חשבון", "הסטוריה"]}
    ]

    for item in data:
        exisiting_item = mycol.find_one({'id': item['id']})
        if exisiting_item == None:
            mycol.insert_one(item)
        elif not exisiting_item['id'] == exisiting_item['id']:
            mycol.insert_one(item)
