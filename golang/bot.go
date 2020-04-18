package main

import (
	"flag"
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"github.com/bradhe/stopwatch"
	"github.com/bwmarrin/discordgo"
)

var (
	Token string
)

func init() {

	flag.StringVar(&Token, "t", "", "BOT-TOKEN-HERE")
	flag.Parse()
}

func main() {

	dg, err := discordgo.New("BOT-TOKEN-HERE")
	if err != nil {
		fmt.Println("error creating Discord session,", err)
		return
	}

	dg.AddHandler(ready)
	dg.AddHandler(messageCreate)

	err = dg.Open()
	if err != nil {
		fmt.Println("error opening connection,", err)
		return
	}

	fmt.Println("Bot is now running.  Press CTRL-C to exit.")
	sc := make(chan os.Signal, 1)
	signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt, os.Kill)
	<-sc
	dg.Close()
}
func ready(s *discordgo.Session, event *discordgo.Ready) {
 usd := discordgo.UpdateStatusData{AFK: false, Status: "idle"}
	s.UpdateStatusComplex(usd)
}
func messageCreate(s *discordgo.Session, m *discordgo.MessageCreate) {
	if m.Author.ID == s.State.User.ID {
		return
	}
	if m.Content == "ping--" {
		msg, err := s.ChannelMessageSend(m.ChannelID, "Pong!")
		if err != nil {
			fmt.Println("error getting message,", err)
			return
		}
		watch := stopwatch.Start()
		s.ChannelMessageEdit(m.ChannelID, msg.ID, "pong")
		watch.Stop()
		s.ChannelMessageDelete(m.ChannelID, msg.ID)
		embed := &discordgo.MessageEmbed{
    Author:      &discordgo.MessageEmbedAuthor{},
    Color:       0x592630,
    Description: "*golang*",
		Footer: &discordgo.MessageEmbedFooter{
			Text: "created by @h ឵឵#8008 <666317117154525185>",
			IconURL: "https://images-ext-2.discordapp.net/external/fnFaY0mx85fCYJgHl2KiOGGf1DuYRiDbFoUhr3IpvFA/https/cdn.discordapp.com/avatars/666317117154525185/da7e7f05282a984e05b625a24acea9b6.webp",
		},
    Fields: []*discordgo.MessageEmbedField{
        &discordgo.MessageEmbedField{
            Name:   "Message Edit Latency",
            Value:  watch.String(),
            Inline: false,
        },
    },
    Image: &discordgo.MessageEmbedImage{
        URL: "",
    },
    Thumbnail: &discordgo.MessageEmbedThumbnail{
        URL: "https://cdn.discordapp.com/attachments/676846050228568090/677256001837334578/alphabet-blocks-icon.png",
    },
    Title:     "Pong",
}
		s.ChannelMessageSendEmbed(m.ChannelID, embed)
	}
	if m.Content == "stopgo--" {
		s.ChannelMessageSend(m.ChannelID, "cya")
		s.Close()
		fmt.Println("bot closed")
		os.Exit(0)
	}
	if m.Content == "kys--" {
		s.ChannelMessageSend(m.ChannelID, "Bye! ***-go***")
		s.Close()
		fmt.Println("bot closed")
		os.Exit(0)
	}
	}
