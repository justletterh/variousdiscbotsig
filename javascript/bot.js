const Discord = require('discord.js');
const client = new Discord.Client();
//part of the eval cmd
function clean(text) {
	if (typeof(text) === "string")
		return text.replace(/`/g, "`" + String.fromCharCode(8203)).replace(/@/g, "@" + String.fromCharCode(8203));
	else
		return text;
}
//replace this with your id
myid = "666317117154525185";
//the on ready event, prints in the console and sets the status when the bot is logged in
client.on('ready', () => {
	client.user.setStatus('idle');
	console.log(`We have logged in as ${client.user.tag}`);
	console.startlat = "global";
	setTimeout(() => {
		startlat = client.ws.ping;
	}, 0);
});

//the on message event, this is what tells the bot to respond to messages
client.on('message', message => {
	if (!message.guild) return;
	if (message.content.startsWith('stopjs--')) {
		message.channel.send("bye");
		setTimeout(() => {
			client.destroy();
		}, 0);
	}
	//kills the bot
	if (message.content.startsWith('kys--')) {
		message.channel.send("Bye! ***-javascript***");
		setTimeout(() => {
			client.destroy();
		}, 0);
	}
	//kicks a member
	if (message.content.startsWith('kick--')) {
		const user = message.mentions.users.first();
		if (user) {
			const member = message.guild.member(user);
			if (member) {
				member
					.kick('Optional reason that will display in the audit logs')
					.then(() => {
						message.channel.send(`Successfully kicked ${user.tag}`);
					})
					.catch(err => {
						message.channel.send('I was unable to kick the member');
						console.error(err);
					});
			} else {
				message.channel.send("That user isn't in this guild!");
			}
		} else {
			message.channel.send("You didn't mention the user to kick!");
		}
	}
	//bans a member
	if (message.content.startsWith('ban--')) {
		const user = message.mentions.users.first();
		if (user) {
			const member = message.guild.member(user);
			if (member) {
				member
					.ban({
						reason: 'They were bad!',
					})
					.then(() => {
						message.channel.send(`Successfully banned ${user.tag}`);
					})
					.catch(err => {
						message.channel.send('I was unable to ban the member');
						console.error(err);
					});
			} else {
				message.channel.send("That user isn't in this guild!");
			}
		} else {
			message.channel.send("You didn't mention the user to ban!");
		}
	}
	const args = message.content.split(" ").slice(1);

	//runs js code
	if (message.content.startsWith("js--")) {
		if (message.author.id !== myid) return;
		try {
			const code = args.join(" ");
			let evaled = eval(code);

			if (typeof evaled !== "string")
				evaled = require("util").inspect(evaled);

			message.channel.send(clean(evaled), {
				code: "xl"
			});
		} catch (err) {
			message.channel.send(`\`ERROR\` \`\`\`xl\n${clean(err)}\n\`\`\``);
		}
	}
	//displays latency
	if (message.content.startsWith('ping--')) {
		var h = client.users.cache.get(myid);
		const embed = {
			"title": "Pong",
			"description": "*javascript*",
			"color": 0x592630,
			"footer": {
				"icon_url": `${h.avatarURL()}`,
				"text": `created by @${h.username}#${h.discriminator} <${myid}>`
			},
			"thumbnail": {
				"url": "https://cdn.discordapp.com/attachments/676846050228568090/677256001837334578/alphabet-blocks-icon.png"
			},
			"fields": [{
					"name": "Latency Now",
					"value": `${client.ws.ping}ms`
				},
				{
					"name": "Latency At Startup",
					"value": `${startlat}ms`
				}
			]
		};
		message.channel.send({
			embed
		});
	}
});

//runs the bot
client.login('BOT-TOKEN-HERE');
