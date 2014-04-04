### Find Under Expander for Sublime Text 3

#### About
This is a Sublime Text 3 Plugin which fixes buges and improves original Sublime Text `find_under_expand` and `find_under_expand_skip` commands.

#### Manual Installation

###### Mac

    git clone https://github.com/odetinin/Find-Under-Expander.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Find\ Under\ Expander

###### Linux

    git clone https://github.com/odetinin/Find-Under-Expander.git ~/.config/sublime-text-3/Packages/Find\ Under\ Expander

###### Windows

    git clone https://github.com/odetinin/Find-Under-Expander.git %APPDATA%/Sublime\ Text\ 3/Packages/Find\ Under\ Expander

#### Usage

###### Commands:

    {
        "caption": "FindUnderExpander: Add to Selection",
        "command": "find_under_expander_quick_add"
    }, {
        "caption": "FindUnderExpander: Skip Selection",
        "command": "find_under_expander_skip"
    }, {
        "caption": "FindUnderExpander: Add Word to Selection",
        "command": "find_under_expander_quick_add_word"
    }, {
        "caption": "FindUnderExpander: Undo Last Selection",
        "command": "find_under_expander_undo"
    }

###### Hotkeys:

    {
        "keys": ["super+d"],
        "command": "find_under_expander_quick_add"
    }, {
        "keys": ["super+l"],
        "command": "find_under_expander_quick_add_word"
    }, {
        "keys": ["super+k", "super+d"],
        "command": "find_under_expander_skip"
    }, {
        "keys": ["super+k", "super+u"],
        "command": "find_under_expander_undo"
    }
