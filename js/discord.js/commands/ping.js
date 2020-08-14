exports.run = async (bot, client, message, args) => {
  const m = await message.channel.send("Ping?");
  m.edit(`Pong!\n${m.createdTimestamp - message.createdTimestamp}ms :hourglass:`);
}
exports.help = {
  name: "ping",
  aliases: ["p"]
}
