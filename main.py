from services.util.scraper import count_videos
import services.util.printer as printer
import entities.Folder as Folder
from linkfile import link

printer.print_starting()
root = Folder.Folder('root')

count_videos(link, root)

printer.print_finished()

printer.print_start_current()
root.print_folder_content()

root.to_json_file()

root.compare_to_last_from_log()

printer.print_start_comparison()
root.print_folder_content()
