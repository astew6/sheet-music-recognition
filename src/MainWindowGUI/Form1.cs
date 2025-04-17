namespace MainWindowGUI
{
    public partial class sheetMusicToMusicXML : Form
    {
        public sheetMusicToMusicXML()
        {
            InitializeComponent();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                outputPathLabel.Text = saveFileDialog1.FileName;
            }
        }

        private void uploadPictureButton_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                inputPathLabel.Text = openFileDialog1.FileName;
            }
        }

        private void reviewEditButton_Click(object sender, EventArgs e)
        {

        }

        private void exportMusicXMLButton_Click(object sender, EventArgs e)
        {

        }
    }
}
