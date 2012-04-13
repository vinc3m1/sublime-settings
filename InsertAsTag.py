import sublime
import sublime_plugin

class InsertAsTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            self.view.sel().clear()
            word_reg = self.view.word(region)
            word = self.view.substr(word_reg)
            offset = 0
            if not word:
                word = "p"
                offset = 1
            s = "<%s></%s>" % (word, word)
            self.view.replace(edit, word_reg, s)
            self.view.sel().clear()
            if region.a < region.b:
                self.view.sel().add(sublime.Region(region.b + 2 + offset))
            else:
                self.view.sel().add(sublime.Region(region.a + 2 + offset))
            self.view.show(self.view.sel())
