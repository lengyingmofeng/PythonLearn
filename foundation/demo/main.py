import asyncio
import nonebot
import src.lib.xiaobei.xiaobei  as xiaobei
import src.lib.xiaobei.xiaobeiUser as  xiaobeiUser
from src.lib.common import ServiceException
from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone='Asia/Shanghai')

async def ScheduledDakaTasks(qq):
    print(f'{qq}开始执行定时任务')
    user = xiaobeiUser.getUser(qq)
    bot = nonebot.get_bot()
    try:
        student = xiaobei.Student(user.username, user.password)
        daka = student.daka()
        DakaInfo = student.GetdakaInfo()
        result = '打卡状态:' + daka + '\n' + '打卡信息:' + DakaInfo
    except ServiceException as e:
        result = e.message
    await bot.send_private_msg(message=result, user_id=qq)


def AddScheduledTask(qq):
    from src.plugins.task import scheduler
    job = scheduler.get_job(qq)
    if job is None:
        u = xiaobeiUser.getUser(qq=qq)
        time = u.talk_date
        if time:
            scheduler.add_job(ScheduledDakaTasks(u.id), 'cron', minute=time.minute, hour=time.hour, second=time.second,
                              id=u.id)
            print(f'{u.id}添加定时任务成功')
        else:
            raise ServiceException('用户还没设置时间，请用户设置时间')
    else:
        u = xiaobeiUser.getUser(qq=qq)
        time = u.talk_date
        if time:
            scheduler.remove_job(job_id=qq)
            scheduler.add_job(ScheduledDakaTasks, 'cron', minute=time.minute, hour=time.hour, second=time.second,
                              args=[u.id], id=u.id)
            print(f'{u.id}修改定时任务成功')
        else:
            raise ServiceException('用户还没设置时间，请用户设置时间')


# 删除定时任务
def DeleteScheduledTask(qq):
    from src.plugins.task import scheduler
    job = scheduler.get_job(qq)
    if job:
        scheduler.remove_job(qq)
    else:
        raise ServiceException(f'{qq}没有定时打卡的任务 无需删除')


# 添加定时任务初始化
def AddScheduledTasks():
    from src.plugins.task import scheduler
    for u in xiaobeiUser.getUsers():
        time = u.talk_date
        if time:
            scheduler.add_job(ScheduledDakaTasks, 'cron', minute=time.minute, hour=time.hour, second=time.second,
                              args=[u.id], id=u.id)
            print(f"添加{u.id}任务成功")



