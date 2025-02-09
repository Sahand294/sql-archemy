class Search_Member:
    @staticmethod
    def search_member_by_name(name,member_list):
        try:
            for i in member_list:
                if member_list[i]['name'] == name:
                    return member_list[i]
        except:
            raise Exception('no such member!')

    @staticmethod
    def search_member_by_id(id,member_list):
        try:
            return  member_list[id]
        except:
            raise Exception('no such member!')

    @staticmethod
    def check_if_member_Exists(member_id,member_list):
        if member_id not in member_list:
            raise ValueError(f'there is no such member')