require 'discordrb'
require "discordrb/webhooks"
auth = 'BOT-TOKEN-HERE'
bot = Discordrb::Bot.new token: auth
myid = 666317117154525185
lgsid = 575500747014144000
bot.ready do
bot.update_status("idle", nil, nil)
end
bot.message(with_text: 'ping--') do |event|
m = event.respond('ping?')
t = Time.now - event.timestamp
t = t*1000
m.edit "ping? #{t}ms"
m.delete
curbot = bot.user(bot.profile.id)
h = bot.user(myid)
event.channel.send_embed do |embed|
embed.title = 'Pong'
embed.description = '*ruby*'
embed.fields = [Discordrb::Webhooks::EmbedField.new(name: 'Message Edit Latency',value: "#{t}ms",inline: false)]
embed.footer = Discordrb::Webhooks::EmbedFooter.new(icon_url: "#{h.avatar_url}",text: "created by @#{h.username}##{h.discrim} <#{myid}>")
embed.color = "#592630"
embed.thumbnail = Discordrb::Webhooks::EmbedThumbnail.new(url: curbot.avatar_url)
end
end
bot.message(with_text: 'stopruby--') do |event|
event.respond('i want to kill me too, dw :thumbsup:')
exit
end
bot.message(with_text: 'kys--') do |event|
event.respond('Bye! ***-ruby***')
exit
end
bot.message do |event|
if event.message.author.id != myid and event.message.author.id != lgsid
if event.message.content.start_with?('hook--')
event.respond "no"
end
end
if event.message.author.id == myid or event.message.author.id == lgsid
msg = event.message.content
if msg.start_with?('hook--')
curwebhook = Discordrb::API::Channel.create_webhook "Bot #{auth}",event.message.channel.id,'Alphabet Webhook(bot.rb)'
msgtosend = msg[6..msg.index('|')-1]
event.message.delete
hookid = msg[msg.index('|')+1..msg.length]
hookid = JSON.parse(Discordrb::API::User.resolve "Bot #{auth}",Integer(hookid))
hookid = Discordrb::User.new hookid,bot
curwebhookobj = Discordrb::Webhook.new(JSON.parse(curwebhook), bot)
curwebhookinit = Discordrb::Webhooks::Client.new(token: curwebhookobj.token,id: curwebhookobj.id)
curwebhookinit.execute do |builder|
builder.content = msgtosend
builder.username = hookid.username
builder.avatar_url = hookid.avatar_url
end
Discordrb::API::Webhook.delete_webhook "Bot #{auth}",curwebhookobj.id
end
end
end
bot.run
