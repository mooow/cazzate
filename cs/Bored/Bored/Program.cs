using System;
using System.Text;
using System.Threading;

namespace Bored
{
    class Bored
    {
        private const string _formatHoursMinutesSeconds = "{0:hh':'mm':'ss}",
            _formatMinutesSeconds = "{0:mm':'ss}";

        static string GetFormat(TimeSpan timeSpan) =>
            timeSpan.Hours > 0 ? _formatHoursMinutesSeconds : _formatMinutesSeconds;

        static void PrintTimeSpan(TimeSpan timeSpan) => Console.Write(GetFormat(timeSpan), timeSpan);

        static void ClearLine() => Console.Write(_formatLineClear);


        static readonly string _formatLineClear =
            new StringBuilder().Append('\r').Append(' ', Console.WindowWidth).Append('\r').ToString();


        static DateTime GetDateTime()
        {
            DateTime dateTime;
            bool valid;
            do
            {
                ClearLine();
                Console.Write("When do you finish?    ");
                valid = DateTime.TryParse(Console.ReadLine(), out dateTime);
                Console.CursorTop--;
            } while (!valid);

            return dateTime;
        }

        static void Main()
        {
            DateTime target;
            TimeSpan diff;

            target = GetDateTime();

            Console.CursorVisible = false;
            do
            {
                diff = target - DateTime.Now;
                ClearLine();
                PrintTimeSpan(diff);
                Thread.Sleep(500);
            } while (diff.TotalSeconds > 0);
        }
    }
}