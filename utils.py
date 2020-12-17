import datetime


class DataConverter:
    @staticmethod
    def make_str_from_dict(post_dict):
        post_data_str = ''
        for data_name in post_dict:
            data_value = post_dict[data_name]
            post_data_str += f'{data_value};'
        return post_data_str[:len(post_data_str) - 1]

    @staticmethod
    def make_dict_from_str(data_str):
        dict_order = ['UNIQUE_ID', 'post URL', 'username', 'user karma', 'user cake day', 'post karma', 'comment karma',
                      'post date', 'number of comments', 'number of votes', 'post category']
        post_data = data_str.replace('\n', '').split(';')
        post_dict = {}
        for ind in range(len(dict_order)):
            post_dict[dict_order[ind]] = post_data[ind]
        return post_dict

    @staticmethod
    def convert_date(date_str):
        """Take a string containing time lapse between publishing post and current time.

        ('just now', '7 days ago', '1 month ago', etc.). Convert it to the date when the post was published.
        """
        if 'just now' in date_str or 'hour' in date_str:
            days = 0
        elif 'month' in date_str:
            days = 31
        else:
            days = int(date_str.split()[0])
        date = datetime.datetime.today() - datetime.timedelta(days=days)
        return date.strftime("%d.%m.%Y")


def check_duplicates(post_data_str, posts_list):
    sent_id = post_data_str[:32]
    for post_str in posts_list:
        stored_id = post_str[:32]
        if sent_id == stored_id:
            return
    return True


def find_line_index(sent_id, posts_list):
    for ind, post_str in enumerate(posts_list):
        stored_id = post_str[:32]
        if sent_id == stored_id:
            return ind
    return


def parse_url(url):
    latest_slash = url[len(url) - 1]
    if latest_slash == '/' and url[:5] == 'posts':
        id_start_index = 6
        if len(url) > id_start_index:
            id = url[id_start_index:len(url) - 1]
            if len(id) == 32:
                return id
            return 404
        return
    return 404