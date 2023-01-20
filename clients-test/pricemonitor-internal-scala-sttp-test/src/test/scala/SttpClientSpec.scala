import HttpServerTest.createServer
import com.patagona.pricemonitor.client.api.ProductsApi
import com.patagona.pricemonitor.client.core.BasicCredentials
import com.patagona.pricemonitor.client.core.BearerToken
import com.patagona.pricemonitor.client.core.HttpException
import com.patagona.pricemonitor.client.core.SttpSerializer
import com.patagona.pricemonitor.client.core.ApiInvoker._
import com.sun.net.httpserver.HttpServer
import org.scalatest.Assertion
import org.scalatest.flatspec.AsyncFlatSpec
import org.scalatest.matchers.must.Matchers
import sttp.client.asynchttpclient.WebSocketHandler
import sttp.client.SttpBackend
import sttp.client.SttpBackendOptions
import sttp.client.asynchttpclient.future.AsyncHttpClientFutureBackend

import scala.concurrent.Future


class SttpClientSpec extends AsyncFlatSpec with Matchers {
  private implicit val serializer: SttpSerializer = new SttpSerializer()
  private implicit val noToken: Option[BearerToken] = None
  private implicit val auth: Option[BasicCredentials] = None
  private implicit val backend: SttpBackend[Future, Nothing, WebSocketHandler] = AsyncHttpClientFutureBackend(SttpBackendOptions.Default)

  private def withHttpServer(test: (HttpServer, String) => Future[Assertion]) = {
    val (server, url) = createServer
    test(server, url)
  }

  it must "handle the case when request fails with response error" in withHttpServer { (server, baseUrl) =>
    val productsApi = ProductsApi(baseUrl)
    val query = None
    val contractId = "1"
    val result = productsApi.queryProductsVendorV3(contractId, query).result
    recoverToExceptionIf[HttpException](result).map { e =>
      server.stop(0)
      e.statusText must be("Not Found")
      e.statusCode.code must be(404)
    }
  }


}