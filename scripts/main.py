from datetime import datetime
import os

def update_change_log():
    with open('changelog.md','a',encoding='utf-8') as f:
        f.write('updated on {}.\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        
def main():
    update_change_log()
    os.system('git add .')
    
if __name__ == '__main__':
    main()
        