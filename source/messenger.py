from openpyxl import load_workbook


wb = load_workbook('책배송-일지.xlsx', data_only=True)


class BookInfo:
    def __init__(self, original_text):
        self.original_text = original_text  # text that was in Excel file(str)
        self.seriesName = None  # real name of series(str)
        self.bookList = []  # list of number of book([str])


class DropDown:
    def __init__(self):
        self.menus = []     # list of menus([DropDown.Menu])
        self.selectedMenu = None    # selected menu(DropDown.Menu)

    def add_menus(self, title, value):  # add menus
        self.menus.append(self.Menu(title, value))

    def select(self):   # ask which menu user will select
        print("Type index")
        for i in range(0, len(self.menus)):
            print(f"{i+1}. {self.menus[i].title}")

        index = int(input(">>  "))
        self.selectedMenu = self.menus[index-1]
        print(f"You've selected {self.selectedMenu.title}")

    class Menu:     # Menu has two attributes: title(str), value
        def __init__(self, title, value):
            self.title = title  # title is a string that will be shown to user
            self.value = value  # value is a real data of menu


class Tab:
    def __init__(self):
        self.selected_sheet = None  # selected sheet(WorkSheet)
        self.selected_date = None   # selected date(MergedCellRange)
        self.schedule = {}  # schedules on selected date({child number(str) : book code(str)})

    def select_sheet(self):     # select sheet
        dd = DropDown()
        for sheet in wb.worksheets:
            dd.add_menus(sheet.title, sheet)
        dd.select()
        self.selected_sheet = dd.selectedMenu.value

    def get_departure_date(self):   # return every merged date cell's ranges(list of MergedCellRanges)
        departure_date_cells = []
        for mergedCell in self.selected_sheet.merged_cells.ranges:
            if mergedCell.start_cell.column == 1:
                departure_date_cells.append(mergedCell)

        return departure_date_cells

    def select_date(self):  # select merged date cell's range(MergedCellRange)
        departure_date_cells = self.get_departure_date()
        dd = DropDown()
        for dateCell in departure_date_cells:
            date = dateCell.start_cell
            dd.add_menus(f"{date.value.year}-{date.value.month}-{date.value.day}", dateCell)
        dd.select()
        self.selected_date = dd.selectedMenu.value

    def get_schedule(self):
        for i in range(self.selected_date.min_row, self.selected_date.max_row + 1):
            self.schedule[self.selected_sheet[f'D{i}'].value] = self.selected_sheet[f'H{i}'].value


t = Tab()
t.select_sheet()
t.select_date()
t.get_schedule()