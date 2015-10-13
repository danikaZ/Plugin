import sublime, sublime_plugin

"""
    usage:
    Save the file to dir: .config/sublime-text-2/Packages/
    Open the Sublime console by pressing ctrl+`. 
    This is a Python console that has access to theAPI. 
    Enter the following Python to test out the new plugin:
        view.run_command('example')

    Only work with current open window so far
"""

class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")
        # highlight keyword: 
        # "TODO"...more keywords...check for all the windows...list them...
        # keybinding
        new_selection_region = self.view.find_all("TODO")

        print new_selection_region
        self.view.add_regions('TODO', new_selection_region, 'string')
