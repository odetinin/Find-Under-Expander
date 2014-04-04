import sublime
import sublime_plugin
import re

word = ""
word_index = -1
whole_word = True
selections = []

class FindUnderExpanderDeleteCommand(sublime_plugin.EventListener):

    def on_selection_modified(self, view):
        global word, word_index, selections

        cursors = view.sel()

        if cursors[0].size() == 0:
            view.erase_regions("current_line")
            del selections[:]
            word = ""
            word_index = -1
        elif len(cursors) == 1:
            del selections[:]
            word = view.substr(cursors[0])
            selections.append(cursors[0])
            word_index = 0
            view.add_regions("current_line", [selections[word_index]], "string", "bookmark")
        else:
            current_line = view.get_regions("current_line")
            if current_line != []:
                try:
                    list(cursors).index(current_line[0])
                except ValueError:
                    view.erase_regions("current_line")
        return

class FindUnderExpanderAddCommand(sublime_plugin.TextCommand):

    def run(self, edit, skip_index = -1, search_next = True):
        global word, word_index, selections

        cursors = self.view.sel()

        if cursors[0].size() == 0:
            self.view.window().run_command('find_under_expand')
            word = self.view.substr(cursors[0])
            selections.append(cursors[0])
            word_index = 0
            return
        else:
            if len(selections) < len(cursors):
                word = self.view.substr(cursors[0])
                selections = list(cursors)
                word_index = len(selections) - 1
                self.display_current_selection()
                return

        cursors.clear()
        self.view.erase_regions("current_line")

        word_position = selections[word_index].end()

        if skip_index != -1:
            word_position = selections[skip_index].end()
            selections.pop(skip_index)
            if search_next == False:
                if word_index == 0:
                    word_index = len(selections) - 1
                else:
                    word_index -= 1
                if len(selections) > 0:
                    cursors.add_all(selections)
                    self.display_current_selection()
                else:
                    cursors.add(sublime.Region(word_position, word_position))
                return

        search_flags = 0

        if whole_word == False:
            search_term = word.format(re.escape(word))
            search_flags = sublime.LITERAL | sublime.IGNORECASE
        else:
            search_term = "\\b{0}\\b".format(re.escape(word))

        find_result = self.view.find(search_term, word_position, search_flags)

        if find_result.a == -1:
            find_result = self.view.find(search_term, 0, search_flags)

            if find_result.a == -1:
                cursors.add_all(selections)
                self.display_current_selection()
                return

        if find_result not in selections:
            selections.append(find_result)
            word_index = len(selections) - 1
        else:
            word_index = selections.index(find_result)

        cursors.add_all(selections)
        self.display_current_selection()
        return

    def display_current_selection(self):
        self.view.add_regions("current_line", [selections[word_index]], "string", "bookmark")
        self.view.show_at_center(selections[word_index].begin())
        return

class FindUnderExpanderQuickAddCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global whole_word

        whole_word = False
        self.view.window().run_command('find_under_expander_add')
        return

class FindUnderExpanderQuickAddWordCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global whole_word

        whole_word = True
        self.view.window().run_command('find_under_expander_add')
        return

class FindUnderExpanderSkipCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().run_command('find_under_expander_add', {"skip_index": word_index})
        return

class FindUnderExpanderUndoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().run_command('find_under_expander_add', {"skip_index": word_index, "search_next": False})
        return