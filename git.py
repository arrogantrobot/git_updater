import subprocess

class git(object):
    def pull(self, daemonDir, remote, branch):
        cmd = ['git', 'pull', remote, branch]
        p = subprocess.Popen(cmd, cwd=daemonDir)
        p.wait()

if __name__ == "__main__":
    g = git()
    g.pull("/home/rob/git/test", "origin", "master")
