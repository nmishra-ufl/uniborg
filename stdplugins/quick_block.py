from telethon.tl.functions.messages import ReportSpamRequest, DeleteHistoryRequest
from telethon.tl.functions.contacts import BlockRequest

@borg.on(borg.admin_cmd(r"nf"))
async def on_quick_block(event):
  await event.delete()
  chat = await event.get_input_chat()

  await borg(ReportSpamRequest(chat))
  await event.respond('@notafile')
  await borg(BlockRequest(chat))
  await borg(DeleteHistoryRequest(chat, max_id=0, revoke=False))
