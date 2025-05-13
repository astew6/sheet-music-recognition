using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using System.Text;
using System.Threading.Tasks;

namespace MainWindowGUI
{
    internal class Music_Component
    {
        private Point startPoint;
        private Point endPoint;
        private int width;
        private int height;
        private string name;

        public Music_Component(): this(0, 0, 0, 0, "") { }

        public Music_Component(int startX, int startY, int endX, int endY, string name)
        {
            this.startPoint.X = startX;
            this.startPoint.Y = startY;
            this.endPoint.X = endX;
            this.endPoint.Y = endY;
            this.width = endPoint.X - startPoint.X;
            this.height = endPoint.Y - startPoint.Y;
            this.name = name;
        }

        // getters

        public int getWidth() { return this.width; }
        public int getHeight() { return this.height; }
        public string getName() { return this.name; }

        // setters

        public void setName(String name) { this.name = name; }

        public void setStartPoint(Point start) { this.startPoint = start; }

        public void setEndPoint(Point end) { this.endPoint = end; }

        public override string ToString()
        {
            return $"Name: {name}, Start: ({startPoint.X},{startPoint.Y}), End: ({endPoint.X},{endPoint.Y}), Width: {width}, Height: {height}";
        }

    }
}
