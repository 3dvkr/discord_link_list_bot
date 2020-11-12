# discord_link_list_bot
Compiles list of messages containing links. Runs manually with no defined command.

It will need two text files to work:
- a file named 'token.txt' which contains the token key on the first line, and the channel id on the second line. The order is important
- the option to create/ read and write a file named 'link_list.txt'. You can change this in the code. It will write the link, and the message id to facilitate troubleshooting

### Next steps:
- isolate the link from the rest of the message
- add a command to be used by all users in a discord
- add the option for users to provide tags/categories for the links
