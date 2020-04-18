require "./src/discordcr"
#defines the bot obj
client = Discord::Client.new(token: "Bot BOT-TOKEN-HERE", client_id: CLIENT-ID-HERE_u64)
#the ready event prints in the console and sets the bot's status when it is logged in
client.on_ready do |payload|
  puts "ready"
  client.status_update("idle")
end
#the message create event tells the bot to reply to messages
client.on_message_create do |payload|
  #displays the latency
  if payload.content.starts_with? "ping--"
    m = client.create_message(payload.channel_id, "Pong!")
    time = Time.utc - payload.timestamp
    lat = time.total_milliseconds
    client.delete_message(m.channel_id, m.id)
    embed = Discord::Embed.new(
  title: "Pong",
  colour: 0x592630,
  description: "*crystal*",
  fields: [
    Discord::EmbedField.new(
      name: "Message Edit Latency",
      value: "#{lat} ms",
    ),
  ],
  thumbnail: Discord::EmbedThumbnail.new(
    url: "https://images-ext-1.discordapp.net/external/jHyN0m_oy7fttZMYg-3WAk010yTxE_5vJ-LvvTjhMHo/https/cdn.discordapp.com/avatars/671804818486198292/51c518a918de05bb895e5b75b72872d9.png?width=80&height=80",
  ),
  footer: Discord::EmbedFooter.new(
    text: "created by @h ឵឵#8008 <666317117154525185>",
    icon_url: "https://images-ext-2.discordapp.net/external/PMCxeJtpgmdHiEIPAfH_LzIFGB6r9kVSazlgreRhToI/https/cdn.discordapp.com/avatars/666317117154525185/da7e7f05282a984e05b625a24acea9b6.png",
  ),
)
    client.create_message(m.channel_id,"", embed)
  end
  #kills the bot
  if payload.content.starts_with? "stopcr--"
    client.create_message(payload.channel_id, "no u")
    client.stop()
  end
  #also kills the bot
  if payload.content.starts_with? "kys--"
    client.create_message(payload.channel_id, "Bye! ***-crystal***")
    client.stop()
  end
end
#runs the bot
client.run
