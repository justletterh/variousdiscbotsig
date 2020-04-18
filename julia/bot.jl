using Discord
c = Client("BOT-TOKEN-HERE")

function handler(c::Client, e::MessageCreate)
    if e.message.content == "ping--"
        reply(c, e.message, "im basically the same as php ***-julia***")
    end
    if e.message.content == "kys--"
        reply(c, e.message, "Bye! ***-julia***")
        close(c)
    end
    if e.message.content == "stopjl--"
        reply(c, e.message, "**WHEEEE**")
        close(c)
    end
    if e.message.content == "chat--asshole"
        reply(c, e.message, "thats right")
    end
    if e.message.content == "chat--you need help"
        reply(c, e.message, "so do you")
    end
    if e.message.content == "chat--bye"
        reply(c, e.message, "__**GREETINGS!!!**__")
    end
end
function ready(c::Client, e::Ready)
    update_status(
    c,
    Nothing(),
    Nothing(),
    "idle",
    false,
)
end

add_handler!(c, MessageCreate, handler)
add_handler!(c, Ready, ready)
open(c)
wait(c)
