<<<<<<< HEAD
# This file must be used using `source bin/activate.fish` *within a running fish ( http://fishshell.com ) session*.
# Do not run it directly.

function _bashify_path -d "Converts a fish path to something bash can recognize"
    set fishy_path $argv
    set bashy_path $fishy_path[1]
    for path_part in $fishy_path[2..-1]
        set bashy_path "$bashy_path:$path_part"
    end
    echo $bashy_path
end

function _fishify_path -d "Converts a bash path to something fish can recognize"
    echo $argv | tr ':' '\n'
end

function deactivate -d 'Exit virtualenv mode and return to the normal environment.'
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        # https://github.com/fish-shell/fish-shell/issues/436 altered PATH handling
        if test (echo $FISH_VERSION | head -c 1) -lt 3
            set -gx PATH (_fishify_path "$_OLD_VIRTUAL_PATH")
        else
            set -gx PATH "$_OLD_VIRTUAL_PATH"
        end
        set -e _OLD_VIRTUAL_PATH
    end

    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME "$_OLD_VIRTUAL_PYTHONHOME"
=======
# This file must be used with ". bin/activate.fish" *from fish* (http://fishshell.org)
# you cannot run it directly

function deactivate  -d "Exit virtualenv and return to normal shell environment"
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        set -gx PATH $_OLD_VIRTUAL_PATH
        set -e _OLD_VIRTUAL_PATH
    end
    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
>>>>>>> dashboard/subjects
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
<<<<<<< HEAD
       and functions -q _old_fish_prompt
        # Set an empty local `$fish_function_path` to allow the removal of `fish_prompt` using `functions -e`.
        set -l fish_function_path

        # Erase virtualenv's `fish_prompt` and restore the original.
        functions -e fish_prompt
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
    end

    set -e VIRTUAL_ENV

    if test "$argv[1]" != 'nondestructive'
        # Self-destruct!
        functions -e pydoc
        functions -e deactivate
        functions -e _bashify_path
        functions -e _fishify_path
    end
end

# Unset irrelevant variables.
deactivate nondestructive

set -gx VIRTUAL_ENV '/home/user/Documents/Awwards/virtual'

# https://github.com/fish-shell/fish-shell/issues/436 altered PATH handling
if test (echo $FISH_VERSION | head -c 1) -lt 3
   set -gx _OLD_VIRTUAL_PATH (_bashify_path $PATH)
else
    set -gx _OLD_VIRTUAL_PATH "$PATH"
end
set -gx PATH "$VIRTUAL_ENV"'/bin' $PATH

# Unset `$PYTHONHOME` if set.
=======
        functions -e fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
    end

    set -e VIRTUAL_ENV
    if test "$argv[1]" != "nondestructive"
        # Self destruct!
        functions -e deactivate
    end
end

# unset irrelevant variables
deactivate nondestructive

set -gx VIRTUAL_ENV "/home/lorraine/Desktop/Moringa_Core/django_project/virtual"

set -gx _OLD_VIRTUAL_PATH $PATH
set -gx PATH "$VIRTUAL_ENV/bin" $PATH

# unset PYTHONHOME if set
>>>>>>> dashboard/subjects
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

<<<<<<< HEAD
function pydoc
    python -m pydoc $argv
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # Copy the current `fish_prompt` function as `_old_fish_prompt`.
    functions -c fish_prompt _old_fish_prompt

    function fish_prompt
        # Run the user's prompt first; it might depend on (pipe)status.
        set -l prompt (_old_fish_prompt)

        # Prompt override provided?
        # If not, just prepend the environment name.
        if test -n ''
            printf '%s%s' '' (set_color normal)
        else
            printf '%s(%s) ' (set_color normal) (basename "$VIRTUAL_ENV")
        end

        string join -- \n $prompt # handle multi-line prompts
=======
if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # fish uses a function instead of an env var to generate the prompt.

    # save the current fish_prompt function as the function _old_fish_prompt
    functions -c fish_prompt _old_fish_prompt

    # with the original prompt function renamed, we can override with our own.
    function fish_prompt
        # Save the return status of the last command
        set -l old_status $status

        # Prompt override?
        if test -n "(virtual) "            
            printf "%s%s" "(virtual) " (set_color normal)
        else
            # ...Otherwise, prepend env
            set -l _checkbase (basename "$VIRTUAL_ENV")
            if test $_checkbase = "__"
                # special case for Aspen magic directories
                # see http://www.zetadev.com/software/aspen/
                printf "%s[%s]%s " (set_color -b blue white) (basename (dirname "$VIRTUAL_ENV")) (set_color normal)
            else
                printf "%s(%s)%s" (set_color -b blue white) (basename "$VIRTUAL_ENV") (set_color normal)
            end
        end

        # Restore the return status of the previous command.
        echo "exit $old_status" | .
        _old_fish_prompt
>>>>>>> dashboard/subjects
    end

    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end
