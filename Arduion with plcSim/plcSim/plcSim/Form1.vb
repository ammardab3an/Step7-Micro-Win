Public Class Form1
    Private WithEvents S7ProSim As New S7PROSIMLib.S7ProSim
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        S7ProSim.WriteInputPoint(0, 0, I0_0.Checked)
        S7ProSim.WriteInputPoint(0, 1, I0_1.Checked)
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        S7ProSim.Connect()
        S7ProSim.SetScanMode(S7PROSIMLib.ScanModeConstants.ContinuousScan)
        Label1.Text = S7ProSim.GetState()
        Label2.Text = S7ProSim.GetScanMode()
        Timer1.Start()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        SerialPort1.PortName = TextBox1.Text
        SerialPort1.BaudRate = Int(TextBox2.Text)
        SerialPort1.Open()
        Button1.Enabled = True
    End Sub
    Private Sub I0_0_CheckedChanged(sender As Object, e As EventArgs) Handles I0_0.CheckedChanged
        S7ProSim.WriteInputPoint(0, 0, I0_0.Checked)
    End Sub
    Private Sub I0_1_CheckedChanged(sender As Object, e As EventArgs) Handles I0_1.CheckedChanged
        S7ProSim.WriteInputPoint(0, 1, I0_1.Checked)
    End Sub

    Private Sub Timer1_Tick(sender As Object, e As EventArgs) Handles Timer1.Tick
        Dim watch As Stopwatch = Stopwatch.StartNew()
        Dim t As Object
        S7ProSim.ReadOutputPoint(0, 0, S7PROSIMLib.PointDataTypeConstants.S7_Bit, Q0_0.Checked)
        SerialPort1.Write(Int(Q0_0.Checked))
        watch.Stop()
        t = watch.Elapsed.TotalMilliseconds

        Dim _watch As Stopwatch = Stopwatch.StartNew()
        Dim _t As Object
        SerialPort1.Write(1)
        SerialPort1.Write(0)
        _watch.Stop()
        _t = _watch.Elapsed.TotalMilliseconds
    End Sub
End Class
