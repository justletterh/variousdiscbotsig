local discordia = require("discordia")
local client = discordia.Client({logLevel = 3})
local enums = discordia.enums
local myid = "666317117154525185"
client:on(
    "ready",
    function()
        print("We have logged in as " .. client.user.tag)
        client:setStatus("idle")
    end
)
function round(x)
    return x + 0.5 - (x + 0.5) % 1
end
client:on(
    "messageCreate",
    function(message)
      if message.author.id ~= client.user.id then
        if message.content == "ping--" then
            local watch = discordia.Stopwatch()
            local msg = message.channel:send("Pong!")
            watch:start()
            msg:setContent("Pong")
            watch:stop()
            local lat = round(watch.milliseconds) .. "ms"
            msg:delete()
            local h = client:getUser(myid)
            message.channel:send {
                embed = {
                    title = "Pong",
                    thumbnail = {url = client.user.avatarURL},
                    description = "*lua*",
                    fields = {
                        {name = "Message Edit Latency", value = lat, inline = false}
                    },
                    color = discordia.Color.fromRGB(89, 38, 48).value,
                    footer = {
                        text = "created by @" .. h.tag .. " <" .. myid .. ">",
                        icon_url = h.avatarURL
                    }
                }
            }
        end
        if message.content == "stoplua--" then
            message.channel:send("Bye! :smile:")
            client:stop()
        end
        if message.content == "kys--" then
            message.channel:send("Bye! ***-lua***")
            client:stop()
        end
    end
  end
)

client:run("Bot BOT-TOKEN-HERE")
