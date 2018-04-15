#版本控制软件SVN/Git代码库的备份脚本
#/bin/bash
SVNDIR=/data/svn
SVNADMIN=/usr/bin/svnadmin
DATE=`date +%Y-%m-%d`
OLDDATE=`date +%Y-%m-%d -d '-30 days'`
BACKDIR=/data/backup/svn-backup
[ -d $(BACKDIR) ] || mkdir -p $(BACKDIR)
LogFile=$(BACKDIR)/svnbak.log
[ -f $(LogFile) ] || touch $(LogFile)

