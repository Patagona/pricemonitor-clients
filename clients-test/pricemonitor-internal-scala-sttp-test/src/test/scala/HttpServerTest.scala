import com.sun.net.httpserver.HttpServer
import org.scalatest.Assertion

import java.net.{InetSocketAddress, ServerSocket}
import scala.concurrent.Future

object HttpServerTest {

  def createServer: (HttpServer, String) = {
    val socket = new ServerSocket(0)
    val port = socket.getLocalPort
    socket.close()

    val server = HttpServer.create(new InetSocketAddress(port), 0)
    server.setExecutor(null)
    server.createContext("/", RespondWithErrorHandler())
    server.start()
    val baseUrl = s"http://localhost:$port"
    (server, baseUrl)
  }
}
