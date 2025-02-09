class ProjectInfo:
    def __init__(self, status, name, storage, start, end):
        self.status = status
        self.name = name
        self.start = start
        self.end = end
        storage[name] = {'name': name, 'status': status, 'starting time': start, 'ending time': end, 'working': 0}


class StaffInfo:
    def __init__(self, name, projectid, list):
        self.name = name
        if list[projectid]['working'] == 8:
            raise Exception('there is enouth people')
        list[projectid]['working'] += 1
        self.project = list[projectid]
        self.hours = 8

class Hours:
    def __init__(self, id, list):
        hours = 8
        hours /= list[id]['working']
        self.hoursneedtowork = hours

class UpdatedHours:
    def __init__(self,worker,projectname,database):
        worker.hours = Hours(projectname,database).hoursneedtowork
class Show:
    def __init__(self, name, projectname, hours):
        print(f'worker "{name}" is working on project:"{projectname}" for {hours}')


lists = {}
projectx = ProjectInfo('working', 'projectx', lists, 'noverm 6,2024', '2025')
workers = []


javad = StaffInfo('javad', projectx.name, lists)
javad1 = StaffInfo('javad1', projectx.name, lists)
javad2 = StaffInfo('javad2', projectx.name, lists)
javad3 = StaffInfo('javad3', projectx.name, lists)

workers.append(javad)
workers.append(javad1)
workers.append(javad2)
workers.append(javad3)

for i in workers:
    UpdatedHours(i,projectx.name,lists)

for i in workers:
    Show(i.name, projectx.name, i.hours)
