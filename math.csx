using System.Threading;
string[] scripts = Directory.GetFiles(Directory.GetCurrentDirectory(), "*.py");
for (int i = 0; i < scripts.Length; i++)
{
    scripts[i] = Path.GetFileNameWithoutExtension(scripts[i]);
}
List<List<string>> argList = new();
argList.Add(new());
foreach (string arg in Args)
{
    if (scripts.Contains<string>(arg))
    {
        argList.Add(new());
    }
    argList[^1].Add(arg);
}
List<string> arg0 = argList[0];
argList.RemoveAt(0);
string cmd = "";
if (arg0.Count != 0)
{
    cmd = "\"Write-Output\" ";
    foreach (string s0 in arg0)
        cmd += "\"\"\"" + s0 + "\"\"\"" + ' ';
}
List<string> cmdps = new();
foreach (var l in argList)
{
    string cmdp = "\"python\" \"-m\" ";
    foreach (var sc in l)
        cmdp += "\"\"\"" + sc + "\"\"\"" + ' ';
    cmdps.Add(cmdp);
}
if (cmdps.Count != 0)
{
    if (cmd.Length != 0)
        cmd += "\"|\" ";
    cmd += string.Join("\"|\" ", cmdps);
}
var psi = new ProcessStartInfo("powershell", cmd)
{
    RedirectStandardOutput = false,
    RedirectStandardInput = false,
    UseShellExecute = false
};
var proc = Process.Start(psi);
proc.WaitForExit();